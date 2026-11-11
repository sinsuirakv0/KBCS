# 00bcdab4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
