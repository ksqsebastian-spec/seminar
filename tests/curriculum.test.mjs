import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {toolkit} from '../public/toolkit.js';
import {scenario} from '../public/storyboard.js';
const c=JSON.parse(await fs.readFile('public/curriculum.json','utf8'));
const lesson=id=>c.lessons.find(l=>l.id===id);
test('ten chapters form the requested sequence with actionable prompts and checks',async()=>{
 assert.deepEqual(c.lessons.map(l=>l.id),['antwort','recherche','projekt','dateien','browser','excel','dokument','teppich','kalender','spaeter']);
 for(const l of c.lessons){assert.ok(l.mission&&l.outcome&&l.carry);assert.ok(l.demos.length>=2);assert.ok(l.checks.length>=2);assert.ok(!('minutes' in l));for(const d of l.demos){assert.ok(d.action&&d.see);assert.equal(d.visual.length,3);if(d.asset)await fs.access('public/screens/'+d.asset);}}
});
test('generated documents flow across chapters without the old mission PDF',()=>{
 assert.match(JSON.stringify(lesson('recherche')),/Hadi_Steckbrief.txt/);assert.match(JSON.stringify(lesson('projekt')),/Hadi_Steckbrief.txt/);
 assert.equal(lesson('projekt').demos.length,2);
 for(const id of ['browser','excel'])assert.match(JSON.stringify(lesson(id)),/Materialrecherche.xlsx/);
 for(const id of ['excel','dokument'])assert.match(JSON.stringify(lesson(id)),/Schrankkalkulation.xlsx/);
 for(const id of ['teppich','spaeter'])assert.match(JSON.stringify(lesson(id)),/Teppich_Favorit.png/);
 assert.doesNotMatch(JSON.stringify(c),/Mission_Hadi|Plane für einen|Keine Gäste/);
});
test('real sends are addressed to Kerim and follow separate inspection steps',()=>{
 for(const id of ['antwort','kalender','spaeter']){const ds=lesson(id).demos;assert.match(ds.at(-1).prompt,/Nutze das Outlook-Plugin/);assert.match(ds.at(-1).prompt,/Kerim Seehafer/);assert.match(ds.at(-2).prompt,/Zeige/);}
 assert.match(lesson('spaeter').demos[1].prompt,/echte Dateianhänge/);
});
test('scaling keeps setup and transport fixed and applies markup then VAT',()=>{
 assert.deepEqual(scenario(1),{hours:12,cost:1340,net:1608,gross:1913.52});
 assert.equal(scenario(5).hours,52);assert.equal(scenario(5).cost,5860);assert.equal(scenario(5).net,7032);assert.equal(scenario(5).gross,8368.08);
 assert.equal(scenario(10).cost-scenario(5).cost,5*1130);
});
test('reference handbook examples name connected plugins',()=>{
 for(const t of toolkit){for(const f of t.items){assert.ok(f.slice(0,4).every(Boolean));if(['outlook','onedrive'].includes(t.app))assert.match(f[2],/Nutze dafür das .+-Plugin/);}}
});
