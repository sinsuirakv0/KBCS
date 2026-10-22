# 007beabc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007beabc.md)

## 関数情報

~~~json
{
  "address": "007beabc",
  "name": "FUN_007beabc",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a436be9c35f79a777dc05342d2348ecd4494cc36eecc5d01d82ed2b3d7db91c",
  "source_text_sha256": "6a436be9c35f79a777dc05342d2348ecd4494cc36eecc5d01d82ed2b3d7db91c"
}
~~~
## 呼び出し元

- [0078adc4](../0078a/0078adc4.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [007bebf8](../007be/007bebf8.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1183 bytes

~~~c

void FUN_007beabc(undefined8 param_1,undefined8 param_2,undefined4 param_3,undefined4 param_4,
                 ulong *param_5,ulong *param_6)

{
  byte bVar1;
  long lVar2;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  if ((*param_5 & 1) == 0) {
    uStack_58 = param_5[1];
    local_60 = *param_5;
    local_50 = (void *)param_5[2];
    bVar1 = (byte)*param_6;
  }
  else {
    FUN_00418fe0(&local_60,param_5[2],param_5[1]);
    bVar1 = (byte)*param_6;
  }
  if ((bVar1 & 1) == 0) {
    uStack_78 = param_6[1];
    local_80 = *param_6;
    local_70 = (void *)param_6[2];
  }
  else {
    FUN_00418fe0(&local_80,param_6[2],param_6[1]);
  }
  FUN_007bebf8(param_1,param_2,0,param_3,param_4,&local_60,&local_80);
  if ((local_80 & 1) != 0) {
    operator_delete(local_70);
  }
  if ((local_60 & 1) != 0) {
    operator_delete(local_50);
  }
  if (*(long *)(lVar2 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
