# 00bcdab4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd68c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0081.md#compare-12326505fba73c50a54de551d678ead8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0091.md#compare-83bac921495bdd1ddc9d4115688ece24)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdab4",
  "name": "_ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53eee70fa6c0ae2701d736741fcaba50795995a1d4121d185a4452435724ba40",
  "source_text_sha256": "53eee70fa6c0ae2701d736741fcaba50795995a1d4121d185a4452435724ba40"
}
~~~

## 呼び出し元

- [00c5d990](../00c5d/00c5d990.md)

## 呼び出し先

- [00c5aba0](../00c5a/00c5aba0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5bef0](../00c5b/00c5bef0.md)
- [00c5da80](../00c5d/00c5da80.md)

## 疑似コード / UTF-8 1057 bytes

~~~c

void _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE(undefined8 *param_1)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
                    /* try { // try from 00bcdad4 to 00ccdadb has its CatchHandler @ 00bcea50 */
  _ZN8firebase4auth4Auth3appEv(param_1);
  uVar2 = _ZNK8firebase3App14GetPlatformAppEv();
  uVar3 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                    (plVar1,DAT_01126728,DAT_01126738,uVar2);
                    /* try { // try from 00bcdb04 to 00ccdb17 has its CatchHandler @ 00bcea30 */
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
                    /* try { // try from 00bcdb18 to 00ccdb1f has its CatchHandler @ 00bcea40 */
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar3);
                    /* WARNING: Could not recover jumptable at 0x00bcdb40. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  return;
}

~~~
