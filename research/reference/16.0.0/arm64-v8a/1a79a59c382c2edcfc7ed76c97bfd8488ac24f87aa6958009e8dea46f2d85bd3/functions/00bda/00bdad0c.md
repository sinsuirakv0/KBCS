# 00bdad0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdad0c",
  "name": "_ZN8firebase4auth17PhoneAuthProvider11GetInstanceEPNS0_4AuthE",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54c8f5d666358d6ad197050ff8a09a74bdb1dbe905b2cfac0b7dd6d170abd929",
  "source_text_sha256": "54c8f5d666358d6ad197050ff8a09a74bdb1dbe905b2cfac0b7dd6d170abd929"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5a7a0](../00c5a/00c5a7a0.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 疑似コード / UTF-8 751 bytes

~~~c

undefined8 * _ZN8firebase4auth17PhoneAuthProvider11GetInstanceEPNS0_4AuthE(long *param_1)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long lVar4;
  undefined8 *puVar5;
  
  puVar5 = (undefined8 *)*param_1;
  if (puVar5[0x4c] == 0) {
    plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*puVar5);
    uVar2 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar1,DAT_011267d0,DAT_011267e0,*(undefined8 *)(*param_1 + 0x1f8));
    puVar3 = (undefined8 *)_Znwm(0x10);
    *puVar3 = 0;
    puVar3[1] = 0;
    puVar5[0x4c] = puVar3;
    lVar4 = (**(code **)(*plVar1 + 0xa8))(plVar1,uVar2);
    plVar1 = (long *)puVar5[0x4c];
    plVar1[1] = lVar4;
    *plVar1 = *param_1;
  }
  return puVar5 + 0x4c;
}

~~~
