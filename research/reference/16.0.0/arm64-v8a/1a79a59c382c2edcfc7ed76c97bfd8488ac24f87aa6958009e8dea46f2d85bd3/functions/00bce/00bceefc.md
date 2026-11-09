# 00bceefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bceefc",
  "name": "_ZN8firebase4auth4Auth17set_language_codeEPKc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884",
  "source_text_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 1051 bytes

~~~c

void _ZN8firebase4auth4Auth17set_language_codeEPKc(long *param_1,long param_2)

{
  long *plVar1;
  long lVar2;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
    lVar2 = 0;
    if (param_2 != 0) {
      lVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
    }
    FUN_00574cac(plVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126350,lVar2);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
    if (lVar2 != 0) {
                    /* try { // try from 00bcef7c to 00ccef83 has its CatchHandler @ 00bcef84 */
                    /* catch() { ... } // from try @ 00bcef7c with catch @ 00bcef84
                       try { // try from 00bcef84 to 00ccefbb has its CatchHandler @ 00bcec24 */
                    /* WARNING: Could not recover jumptable at 0x00bcef88. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar1 + 0xb8))(plVar1,lVar2);
      return;
    }
  }
  return;
}

~~~
