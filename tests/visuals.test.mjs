import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {visuals,visualStage,demoArts,art} from '../public/visuals.js';
import {chapters,stepApps} from '../public/chapters.js';
const plan=JSON.parse(await fs.readFile('public/curriculum.json','utf8'));
test('every chapter has orientation and a complete guided sequence',()=>{
 for(const l of plan.lessons){const c=chapters[l.id];assert.ok(c?.intro&&c?.before&&c?.after);assert.equal(c.flow.length,3);assert.equal(stepApps[l.id].length,l.demos.length);for(const d of l.demos)assert.ok(d.action&&d.see);}
});
test('research and browser actions are distinct stations',()=>{
 const research=plan.lessons.find(x=>x.id==='recherche'),browser=plan.lessons.find(x=>x.id==='browser');
 assert.match(JSON.stringify(research),/Teherani/);assert.match(JSON.stringify(browser),/Filter/);assert.match(JSON.stringify(browser),/In-App-Browser/);assert.match(JSON.stringify(browser),/Materialrecherche.xlsx/);
});
