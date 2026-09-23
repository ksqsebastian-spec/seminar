import { assets } from './assets.js';
const encoder=new TextEncoder();
const headers={'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'same-origin','X-Frame-Options':'DENY','Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'; form-action 'self'; base-uri 'none'"};
const cookieName='seminar_session';
const b64=bytes=>btoa(String.fromCharCode(...bytes)).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const unb64=s=>Uint8Array.from(atob(s.replace(/-/g,'+').replace(/_/g,'/')),c=>c.charCodeAt(0));
async function key(secret){return crypto.subtle.importKey('raw',encoder.encode(secret),{name:'HMAC',hash:'SHA-256'},false,['sign','verify'])}
export async function token(secret,expiry=Math.floor(Date.now()/1000)+43200){const data=String(expiry);return data+'.'+b64(new Uint8Array(await crypto.subtle.sign('HMAC',await key(secret),encoder.encode(data))))}
export async function validToken(value,secret){try{const [expiry,sig,...extra]=value.split('.');if(extra.length||!/^\d+$/.test(expiry)||Number(expiry)<=Date.now()/1000||Number(expiry)>Date.now()/1000+43201)return false;return await crypto.subtle.verify('HMAC',await key(secret),unb64(sig),encoder.encode(expiry))}catch{return false}}
async function equal(a,b){const x=new Uint8Array(await crypto.subtle.digest('SHA-256',encoder.encode(a))),y=new Uint8Array(await crypto.subtle.digest('SHA-256',encoder.encode(b)));let result=0;for(let i=0;i<x.length;i++)result|=x[i]^y[i];return result===0}
function login(message='',next=''){return `<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Willkommen — workshop.</title><style>*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;color:#101116;background:#fff;min-height:100svh;display:grid;place-items:center;padding:30px}main{width:min(100%,500px)}.brand{font-size:26px;font-weight:800;letter-spacing:-1px;margin-bottom:70px}h1{font-size:clamp(50px,10vw,76px);line-height:1.05;letter-spacing:-4px;margin:0 0 25px}h1 span{background:linear-gradient(100deg,#1454ff,#9b40da,#ff786c);background-clip:text;color:transparent}p{color:#666b78;line-height:1.6}label{display:block;margin:30px 0 9px;font-size:14px}input{width:100%;padding:17px;border:1px solid #dadce3;border-radius:12px;font:inherit}button{width:100%;border:0;padding:17px;background:#1454ff;color:white;border-radius:12px;font:inherit;font-weight:600;margin-top:13px;cursor:pointer}input:focus-visible,button:focus-visible{outline:3px solid #8b9eff;outline-offset:4px}.error{color:#b62436;font-size:14px;min-height:22px}</style><main><div class="brand">workshop.</div><h1>Bereit für<br><span>deinen Workday?</span></h1><p>Dein Workshop für KI im Arbeitsalltag.<br>Mitmachen, ausprobieren, weiterkommen.</p><form method="post" action="/login${next?'?next=vorbereitung':''}"><label for="password">Workshop-Passwort</label><input id="password" name="password" type="password" autocomplete="current-password" required maxlength="200" autofocus><button>Workshop öffnen</button><p class="error" role="alert">${message}</p></form></main></html>`}
function response(body,status=200,extra={}){return new Response(body,{status,headers:{...headers,...extra}})}
export default {async fetch(request,env){const url=new URL(request.url);if(!env.WORKSHOP_PASSWORD||!env.SESSION_SECRET)return response('Der Workshop wird gerade eingerichtet.',503);
 const origin=request.headers.get('Origin');const next=url.searchParams.get('next')==='vorbereitung'?'vorbereitung':'';
 if(request.method==='POST'&&(origin!==url.origin||request.headers.get('Sec-Fetch-Site')==='cross-site'))return response('Ungültige Anfrage.',403);
 if(url.pathname==='/login'&&request.method==='POST'){
  if(Number(request.headers.get('Content-Length')||0)>4096)return response('Anfrage zu groß.',413);
  const raw=await request.text();if(raw.length>4096)return response('Anfrage zu groß.',413);
  const password=new URLSearchParams(raw).get('password')||'';
  const allowed=await env.LOGIN_LIMITER.limit({key:request.headers.get('CF-Connecting-IP')||'local'});
  if(!allowed.success)return response(login('Zu viele Versuche. Bitte warte eine Minute.',next),429,{'Content-Type':'text/html; charset=utf-8','Retry-After':'60'});
  if(!(await equal(password,env.WORKSHOP_PASSWORD)))return response(login('Das Passwort stimmt noch nicht. Versuch es erneut.',next),401,{'Content-Type':'text/html; charset=utf-8'});
  return response(null,303,{'Location':next?'/vorbereitung.html':'/','Set-Cookie':`${cookieName}=${await token(env.SESSION_SECRET)}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=43200`});
 }
 if(url.pathname==='/logout'&&request.method==='POST')return response(null,303,{'Location':'/','Set-Cookie':`${cookieName}=; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=0`});
 if(!['GET','HEAD'].includes(request.method))return response('Methode nicht erlaubt.',405,{'Allow':'GET, HEAD'});
 const cookie=request.headers.get('Cookie')?.split(';').map(c=>c.trim()).find(c=>c.startsWith(cookieName+'='))?.slice(cookieName.length+1)||'';
 if(!(await validToken(cookie,env.SESSION_SECRET))){if(url.pathname==='/'||url.pathname==='/login'||url.pathname==='/vorbereitung.html')return response(request.method==='HEAD'?null:login('',url.pathname==='/vorbereitung.html'?'vorbereitung':next),200,{'Content-Type':'text/html; charset=utf-8'});return response('Bitte öffne den Workshop und melde dich an.',401)}
 const path=url.pathname==='/'?'/index.html':url.pathname;
 const asset=assets[path];if(!asset)return response('Diese Seite gibt es nicht.',404);
 const bytes=Uint8Array.from(atob(asset.data),c=>c.charCodeAt(0));
 return response(request.method==='HEAD'?null:bytes,200,{'Content-Type':asset.type,...(path.startsWith('/material/')?{'Content-Disposition':`attachment; filename="${path.split('/').pop()}"`}:{})});
}};
