# 00bdad0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6b80c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b80c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/high-0005.md#compare-6cb1a7921b5d84c5d374b373e9bcd05c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
