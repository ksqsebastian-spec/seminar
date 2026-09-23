import http from 'node:http';
import fs from 'node:fs/promises';
import {webcrypto} from 'node:crypto';
if(!globalThis.crypto)globalThis.crypto=webcrypto;
const vars=Object.fromEntries((await fs.readFile('.dev.vars','utf8')).split('\n').filter(x=>x.includes('=')).map(x=>{const i=x.indexOf('=');return[x.slice(0,i),x.slice(i+1)]}));
let attempts=new Map();const env={...vars,LOGIN_LIMITER:{async limit({key}){const t=Math.floor(Date.now()/60000),k=key+t;const n=(attempts.get(k)||0)+1;attempts.set(k,n);return{success:n<=60}}}};
const port=process.env.PORT||4173;
http.createServer(async(req,res)=>{try{const chunks=[];for await(const c of req)chunks.push(c);const worker=(await import('../dist/worker.mjs?v='+Date.now())).default;const url=`http://localhost:${port}${req.url}`;const request=new Request(url,{method:req.method,headers:req.headers,...(!['GET','HEAD'].includes(req.method)?{body:Buffer.concat(chunks)}:{})});const result=await worker.fetch(request,env);const localHeaders=Object.fromEntries(result.headers);if(localHeaders['set-cookie'])localHeaders['set-cookie']=localHeaders['set-cookie'].replace('; Secure','');res.writeHead(result.status,localHeaders);res.end(Buffer.from(await result.arrayBuffer()))}catch(e){console.error(e);res.writeHead(500);res.end('Local preview error')}}).listen(port,'127.0.0.1',()=>console.log(`Workshop preview: http://localhost:${port}`));
