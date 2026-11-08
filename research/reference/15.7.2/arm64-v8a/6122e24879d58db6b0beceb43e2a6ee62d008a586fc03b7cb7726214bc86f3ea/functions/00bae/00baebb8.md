# 00baebb8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baebb8",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0632f2bdfd414c6a4a1997ba12dc312c6d77812b1583e567044225620d54d960",
  "source_text_sha256": "0632f2bdfd414c6a4a1997ba12dc312c6d77812b1583e567044225620d54d960"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babd60](../00bab/00babd60.md)

## 疑似コード / UTF-8 768 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* try { // try from 00baebd8 to 00caebe3 has its CatchHandler @ 00baed6c */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baebfc to 00caec03 has its CatchHandler @ 00baed58 */
  FUN_00babd60(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
