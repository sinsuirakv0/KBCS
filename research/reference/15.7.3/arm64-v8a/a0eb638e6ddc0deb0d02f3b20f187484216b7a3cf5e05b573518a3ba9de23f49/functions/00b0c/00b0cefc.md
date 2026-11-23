# 00b0cefc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0ce34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0ce34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/alignment_unresolved-0002.md#compare-7ef161438b1fc9030a538a3d550fec8e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cefc",
  "name": "_ZN11flatbuffers17FlatBufferBuilderD2Ev",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2d0c2a69615f351f05fb1bd406710d603d61a2e60a52c95db6b488801fd7b5c",
  "source_text_sha256": "b2d0c2a69615f351f05fb1bd406710d603d61a2e60a52c95db6b488801fd7b5c"
}
~~~

## 呼び出し元

- [00bdea10](../00bde/00bdea10.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdeb10](../00bde/00bdeb10.md)
- [00bdef40](../00bde/00bdef40.md)

## 疑似コード / UTF-8 944 bytes

~~~c

void _ZN11flatbuffers17FlatBufferBuilderD2Ev(long *param_1)

{
  long *plVar1;
  void *pvVar2;
  
  pvVar2 = (void *)param_1[0xb];
  if (pvVar2 != (void *)0x0) {
    _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_17FlatBufferBuilder19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (pvVar2,*(undefined8 *)((long)pvVar2 + 8));
    _ZdlPv(pvVar2);
  }
  pvVar2 = (void *)param_1[5];
                    /* try { // try from 00b0cf2c to 00c0cf33 has its CatchHandler @ 00b0cfa4 */
  if (pvVar2 != (void *)0x0) {
    plVar1 = (long *)*param_1;
    if (plVar1 == (long *)0x0) {
      _ZdaPv(pvVar2);
    }
    else {
      (**(code **)(*plVar1 + 0x18))(plVar1,pvVar2,param_1[4]);
    }
  }
  param_1[5] = 0;
  if (((char)param_1[1] != '\0') && ((long *)*param_1 != (long *)0x0)) {
    (**(code **)(*(long *)*param_1 + 8))();
  }
  *param_1 = 0;
  *(undefined1 *)(param_1 + 1) = 0;
  return;
}

~~~
