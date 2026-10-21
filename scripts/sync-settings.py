from pathlib import Path
import csv, hashlib, io, json, sys

root=Path(sys.argv[1] if len(sys.argv)>1 else '../KBC-rakv0-assets').resolve()
output=Path('ui')
sources={}

def digest(data):return hashlib.sha256(data).hexdigest()
def read_json(path):return json.loads(path.read_text(encoding='utf-8-sig'))
current=read_json(root/'metadata/jp/current.json')
assert current['status']=='verified'
generated=root/current['generatedPath']
manifest_bytes=(generated/'manifest.json').read_bytes()
assert digest(manifest_bytes)==current['manifestSha256']
manifest=json.loads(manifest_bytes)
index_bytes=(generated/'indexes/assets.json').read_bytes()
index_ref=manifest['artifacts']['indexes/assets.json']
assert len(index_bytes)==index_ref['size'] and digest(index_bytes)==index_ref['sha256']
index=json.loads(index_bytes)
for header in [manifest['header'],index['header']]:
    assert all(header[key]==current[key] for key in ['schemaVersion','datasetId','buildId','sourceRegion','versionCode','versionName'])

def read_asset(name):
    entry=index['files'][name]
    path=(root/entry['path']).resolve()
    path.relative_to(root)
    data=path.read_bytes()
    assert len(data)==entry['size'] and digest(data)==entry['sha256'],name
    sources[name]=entry
    return data

def rows(name):return list(csv.reader(io.StringIO(read_asset(name).decode('utf-8-sig'))))
def numeric_rows(name):
    text=read_asset(name).decode('utf-8-sig')
    return [[int(cell.strip()) for cell in line.split('//')[0].split(',') if cell.strip()] for line in text.splitlines() if line.split('//')[0].strip()]

treasures=[]
for campaign in range(3):
    for chapter in range(1,4):
        suffix=str(campaign) if campaign<2 else '2_'+str(chapter-1)
        names=rows('res/Treasure3_'+suffix+'_ja.csv')
        definitions=numeric_rows('Data/treasureData'+suffix+'.csv')
        assert len(names)>=11 and len(definitions)==44
        for group in range(11):
            value,effect,flag=definitions[33+group]
            treasures.append({'id':f'{campaign}-{chapter}-{group}','campaign':campaign,'chapter':chapter,'group':group,'name':names[group][0].strip(),'description':'\n'.join(cell.strip() for cell in names[group][1:] if cell.strip() and cell.strip() not in ['＠','@']),'maximumEffect':value,'effectType':effect,'effectFlag':flag})

names=rows('res/GatyaitemName.csv')
limits=numeric_rows('Data/AbilityData.csv')
items=rows('Data/Gatyaitembuy.csv')
assert len(limits)==10
keys=['cannonAttack','cannonRange','cannonCharge','worker','wallet','castle','research','accounting','study','energy']
facilities=[]
for position,key in enumerate(keys):
    item=60+position
    entry=next(row for row in items if len(row)>7 and row[3]==str(item))
    assert entry[6]=='2' and entry[7]==str(position)
    name,description=names[item][0],names[item][1:]
    image='gatyaitemD_'+str(item)+'_f.png'
    path=output/'icons/facilities'/image;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(read_asset('Image/'+image))
    facilities.append({'id':key,'name':name,'description':'\n'.join(cell.strip() for cell in description if cell.strip() and cell.strip() not in ['＠','@']),'maxLevel':limits[position][2],'maxPlus':limits[position][3],'icon':'/icons/facilities/'+image})

parameters=dict(line.split('\t',1) for line in read_asset('Data/param.tsv').decode('utf-8-sig').splitlines() if '\t' in line)
combatParameters={key:int(parameters[key]) for key in ['battle_super_beast_hunter','battle_super_beast_hunter_df','battle_super_sage_hunter_damage1','battle_super_sage_hunter_damage2','battle_metal_killer_hp_type']}

assert combatParameters['battle_metal_killer_hp_type']==1

cannonParts={}
for part,file in [('base','CC_BaseParts_growth.csv'),('decoration','CC_DecoParts_growth.csv')]:
    groups={}
    effects={0:'red',1:'floating',2:'black',4:'angel',5:'alien',6:'zombie',7:'relic'} if part=='base' else dict(enumerate(['slow','wave','stop','surge','weaken','toxic','curse']))
    for row in rows('Data/'+file)[1:]:
        if not row:continue
        item,effect,level,start,end,easing=map(int,row)
        if item==0:continue
        assert easing==0 and 1<=item<=7 and effect in effects and 0<=start<=end<=10000
        entry=groups.setdefault((item,effect),{'id':item,'effect':effects[effect],'rates':[0]})
        previous=max(1,len(entry['rates'])-1)
        assert level>previous
        for current_level in range(len(entry['rates']),level+1):entry['rates'].append(start+(end-start)*(current_level-previous)//(level-previous))
    cannonParts[part]=list(groups.values())

catalog={'cannonParts':cannonParts,'combatParameters':combatParameters,'schemaVersion':1,'region':current['sourceRegion'],'version':current['versionName'],'versionCode':current['versionCode'],'datasetId':current['datasetId'],'buildId':current['buildId'],'manifestSha256':current['manifestSha256'],'assetIndexSha256':index_ref['sha256'],'sources':sources,'treasures':treasures,'facilities':facilities}
# 配布版では原本のcheckoutやネット接続を必要としない。
(output/'settings-catalog.js').write_text('export default '+json.dumps(catalog,ensure_ascii=True,separators=(',',':'))+';\n',encoding='utf-8')
print(f'Settings: {len(treasures)} treasure groups, {len(facilities)} facilities, {len(sources)} verified inputs')
