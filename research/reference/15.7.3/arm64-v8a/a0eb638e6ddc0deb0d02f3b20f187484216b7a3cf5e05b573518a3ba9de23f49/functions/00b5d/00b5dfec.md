# 00b5dfec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b5df24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5df24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0069.md#compare-0e5219fdbefb19679a8f83932ac5875c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5dfec",
  "name": "_ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f669ae4506e50bb5b7fc09e97699815408f60940c7686f640c42a96f3dfef8df",
  "source_text_sha256": "f669ae4506e50bb5b7fc09e97699815408f60940c7686f640c42a96f3dfef8df"
}
~~~

## 呼び出し元

- [00be0a00](../00be0/00be0a00.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde030](../00bde/00bde030.md)
- [00bde100](../00bde/00bde100.md)
- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0c10](../00be0/00be0c10.md)
- [00be0c20](../00be0/00be0c20.md)
- [00be0c30](../00be0/00be0c30.md)
- [00be0c50](../00be0/00be0c50.md)
- [00be0c70](../00be0/00be0c70.md)

## 関連文字列（未確認候補）

~~~text
"g_initialized_count"
~~~

## 疑似コード / UTF-8 1841 bytes

~~~c

void _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE
               (undefined8 param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  long lVar2;
  
                    /* try { // try from 00b5dfec to 00c5dff7 has its CatchHandler @ 00b5e558 */
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*param_2);
  if ((*(byte *)(param_2 + 0x28) & 1) == 0) {
    lVar2 = (long)param_2 + 0x141;
  }
  else {
    lVar2 = param_2[0x2a];
  }
  _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc(uVar1,lVar2);
                    /* try { // try from 00b5e044 to 00c5e067 has its CatchHandler @ 00b5e560 */
  FUN_00551e14(uVar1,param_2[0x41],DAT_010a14c0);
  FUN_00551e14(uVar1,param_2[0x3f],DAT_010a1420,param_2[0x41]);
  FUN_00551e14(uVar1,param_2[0x42],DAT_010a14e8);
  FUN_00551e14(uVar1,param_2[0x3f],DAT_010a1430,param_2[0x42]);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x41);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x42);
                    /* try { // try from 00b5e0b4 to 00c5e0d7 has its CatchHandler @ 00b5e58c */
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x40);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,param_2 + 0x3f);
  if (DAT_010a14f8 == 0) {
    _ZN8firebase9LogAssertEPKcz("g_initialized_count");
  }
  DAT_010a14f8 = DAT_010a14f8 + -1;
  if (DAT_010a14f8 != 0) {
                    /* try { // try from 00b5e10c to 00c5e12f has its CatchHandler @ 00b5e588 */
    return;
  }
  _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv(uVar1);
  _ZN8firebase4util9TerminateEP7_JNIEnv(uVar1);
  return;
}

~~~
