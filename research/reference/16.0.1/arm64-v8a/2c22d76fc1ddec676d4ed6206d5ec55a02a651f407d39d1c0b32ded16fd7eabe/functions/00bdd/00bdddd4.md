# 00bdddd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd9ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0085.md#compare-10f86b6bdaf455e240684731e466ca0b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0095.md#compare-bec1de1c10f998035360c941bf5ad41d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddd4",
  "name": "_ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c0e6ef6bf02f13059bdcaad4210353d0f35f1bcd726196cafd3b5adb004f949",
  "source_text_sha256": "5c0e6ef6bf02f13059bdcaad4210353d0f35f1bcd726196cafd3b5adb004f949"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aef0](../00c5a/00c5aef0.md)
- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126e28 == 0) {
    DAT_01126e28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
                    /* try { // try from 00bdde14 to 00cdde1f has its CatchHandler @ 00bdeecc */
  }
                    /* try { // try from 00bdde20 to 00cdea5f has its CatchHandler @ 00bd6f4c */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126e28,&DAT_00310230,1,&DAT_01126e58,
             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
  return;
}

~~~
