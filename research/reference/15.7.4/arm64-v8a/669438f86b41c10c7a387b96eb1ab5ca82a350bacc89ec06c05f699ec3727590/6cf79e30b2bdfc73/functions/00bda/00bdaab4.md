# 00bdaab4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdaab4.md)

## 関数情報

~~~json
{
  "address": "00bdaab4",
  "name": "FUN_00bdaab4",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82035333d70fc7d1fd7207874d7e08a5463009fabd7f120c6f28f397f9e3980f",
  "source_text_sha256": "82035333d70fc7d1fd7207874d7e08a5463009fabd7f120c6f28f397f9e3980f"
}
~~~
## 呼び出し元

- [00bda3c8](../00bda/00bda3c8.md)

## 呼び出し先

- [00bd75d0](../00bd7/00bd75d0.md)
- [00bd94b0](../00bd9/00bd94b0.md)
- [00bda7cc](../00bda/00bda7cc.md)
- [00bdac1c](../00bda/00bdac1c.md)

## 疑似コード 1/1 / UTF-8 2015 bytes

~~~c

undefined8
FUN_00bdaab4(undefined8 param_1,ulong param_2,long param_3,ulong param_4,long param_5,
            undefined8 param_6)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  ulong uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long local_88;
  undefined1 auStack_80 [8];
  ulong local_78;
  long local_70;
  undefined1 local_68;
  
                    /* catch() { ... } // from try @ 00bda9ec with catch @ 00bdaabc */
  lVar4 = param_3 + (param_4 & 0xffffffff);
  uVar1 = FUN_00bda7cc(param_1,param_3,lVar4,auStack_80);
  if (((uVar1 & 1) != 0) && (local_78 != 0)) {
    lVar2 = FUN_00bdac1c(local_68);
    lVar7 = 0;
    do {
      if (local_78 < 2) {
        lVar8 = lVar7 * lVar2;
        break;
      }
      uVar6 = local_78 >> 1;
      lVar8 = (uVar6 + lVar7) * lVar2;
      local_88 = local_70 + lVar8;
      uVar1 = FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
      uVar5 = local_78 - uVar6;
      local_78 = uVar6;
                    /* try { // try from 00bdab64 to 00cdabb3 has its CatchHandler @ 00bdab64
                       catch() { ... } // from try @ 00bdab64 with catch @ 00bdab64
                       catch() { ... } // from try @ 00bdac08 with catch @ 00bdab64 */
      if (uVar1 < param_2) {
        local_78 = uVar5;
        lVar7 = uVar6 + lVar7;
      }
    } while (uVar1 != param_2);
    local_88 = local_70 + lVar8;
    FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
                    /* try { // try from 00bdabb4 to 00cdac07 has its CatchHandler @ 00bdac08 */
    uVar3 = FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
    lVar4 = FUN_00bd75d0(param_1,uVar3,param_5,param_6,0);
    if (((lVar4 == 0) && (*(ulong *)(param_5 + 0x18) <= param_2)) &&
       (param_2 < *(ulong *)(param_5 + 0x20))) {
      return 1;
    }
  }
                    /* catch() { ... } // from try @ 00bdabb4 with catch @ 00bdac08
                       try { // try from 00bdac08 to 00cdac37 has its CatchHandler @ 00bdab64 */
  return 0;
}

~~~
