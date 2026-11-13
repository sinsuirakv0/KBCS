# 00b2fddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b2fddc",
  "name": "FUN_00b2fddc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54c4bf73545be37d03da2edf8f9fbf6d4ac0792797d3201860d6b186a0e5a373",
  "source_text_sha256": "54c4bf73545be37d03da2edf8f9fbf6d4ac0792797d3201860d6b186a0e5a373"
}
~~~

## 呼び出し元

- [00b2faa8](../00b2f/00b2faa8.md)

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [00b308b4](../00b30/00b308b4.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 1439 bytes

~~~c

void FUN_00b2fddc(undefined8 param_1,undefined8 param_2,ulong *param_3,undefined8 param_4,
                 undefined4 param_5)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  void *pvVar4;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
                    /* try { // try from 00b2fde4 to 00c2fdeb has its CatchHandler @ 00b2fe58 */
                    /* try { // try from 00b2fdec to 00c2fedb has its CatchHandler @ 00b2fd70 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if ((*param_3 & 1) == 0) {
    uStack_78 = param_3[1];
    local_80 = *param_3;
    local_70 = (void *)param_3[2];
  }
  else {
    FUN_0043bb60(&local_80,param_3[2],param_3[1]);
  }
  uVar2 = local_80;
  uVar3 = uStack_78;
  pvVar4 = local_70;
  if ((local_80 & 1) != 0) {
    FUN_0043bb60(&local_60,local_70,uStack_78);
    uVar2 = local_60;
    uVar3 = uStack_58;
    pvVar4 = local_50;
  }
  local_50 = pvVar4;
  uStack_58 = uVar3;
  local_60 = uVar2;
  FUN_00b308b4(param_1,param_2,0,&local_60,param_4,param_5);
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* catch() { ... } // from try @ 00b2fdd8 with catch @ 00b2feac */
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
