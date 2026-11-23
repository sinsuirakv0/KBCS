# 00aeadd4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aead90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0064.md#compare-a889ab6a2bbc6b3ae2e898a4d06e64c7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeadd4",
  "name": "_ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1",
  "source_text_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2215 bytes

~~~c

bool _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0858 == '\0') {
                    /* try { // try from 00aeae0c to 00beb20f has its CatchHandler @ 00aeae0c
                       catch() { ... } // from try @ 00aeae0c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb3e8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb554 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aebac8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec180 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec4d8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca18 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca9c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aecd6c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aedb34 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeed74 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef3fc with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef710 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef7e0 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1090 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1410 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1510 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1644 with catch @ 00aeae0c */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0850,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0858 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0858;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~
