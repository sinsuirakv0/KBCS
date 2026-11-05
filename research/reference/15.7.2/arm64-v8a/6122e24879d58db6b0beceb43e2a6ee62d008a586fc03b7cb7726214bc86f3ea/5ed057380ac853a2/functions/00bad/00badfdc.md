# 00badfdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00badfdc.md)

## 関数情報

~~~json
{
  "address": "00badfdc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c204010534c030bf8bc1c310ae6da38e01859de6d9549f120772f5f71d735ff",
  "source_text_sha256": "1c204010534c030bf8bc1c310ae6da38e01859de6d9549f120772f5f71d735ff"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1238 bytes

~~~c

undefined1
_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
          (long param_1,undefined8 param_2,char *param_3,char *param_4,ulong *param_5,
          ushort *param_6,ushort *param_7,undefined8 *param_8)

{
  ushort uVar1;
  undefined1 uVar2;
  ushort *puVar3;
  ulong uVar4;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == -1)) {
    param_3 = param_3 + (ulong)(param_3[1] == -2) * 2;
  }
  if (param_3 < param_4 + -1) {
    uVar4 = *(ulong *)(param_1 + 0x10);
    uVar2 = 2;
    puVar3 = param_6;
    while (param_6 = puVar3, puVar3 < param_7) {
                    /* try { // try from 00bae02c to 00cae04f has its CatchHandler @ 00bae59c */
      if (((param_3[1] & 0xf8U) == 0xd8) || (uVar1 = CONCAT11(param_3[1],*param_3), uVar4 < uVar1))
      goto LAB_00bae064;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00bae064:
  *param_5 = (ulong)param_3;
                    /* try { // try from 00bae068 to 00cae06f has its CatchHandler @ 00bae568 */
  *param_8 = param_6;
  return uVar2;
}

~~~
