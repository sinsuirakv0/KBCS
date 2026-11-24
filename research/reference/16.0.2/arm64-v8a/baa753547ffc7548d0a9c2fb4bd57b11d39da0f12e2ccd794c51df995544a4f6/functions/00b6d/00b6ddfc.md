# 00b6ddfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6dd60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0038.md#compare-63e57e5da19504bb8db40a4ba7cca546)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0033.md#compare-c120d63d7f8b0d8217f81f836f47df7a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ddfc",
  "name": "_ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc57a5e42dc2f7608f2264d076c0519886baf94a98cc5f0202c48395eb4678cd",
  "source_text_sha256": "cc57a5e42dc2f7608f2264d076c0519886baf94a98cc5f0202c48395eb4678cd"
}
~~~

## 呼び出し元

- [00c5b9a0](../00c5b/00c5b9a0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5b940](../00c5b/00c5b940.md)
- [00c5bb60](../00c5b/00c5bb60.md)

## 疑似コード / UTF-8 1086 bytes

~~~c

void _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev(long param_1)

{
  undefined8 *puVar1;
  undefined8 *__ptr;
  void *__ptr_00;
  
  __ptr = *(undefined8 **)(param_1 + 0x18);
  puVar1 = *(undefined8 **)(param_1 + 0x20);
  if (__ptr != puVar1) {
    do {
      __ptr_00 = (void *)*__ptr;
      if (__ptr_00 != (void *)0x0) {
        if ((*(byte *)((long)__ptr_00 + 0xc0) & 1) != 0) {
          _ZdlPv(*(void **)((long)__ptr_00 + 0xd0));
        }
        _ZN11flatbuffers10DefinitionD2Ev(__ptr_00);
        _ZdlPv(__ptr_00);
        puVar1 = *(undefined8 **)(param_1 + 0x20);
      }
      __ptr = __ptr + 1;
    } while (__ptr != puVar1);
    __ptr = *(undefined8 **)(param_1 + 0x18);
  }
  if (__ptr != (undefined8 *)0x0) {
    *(undefined8 **)(param_1 + 0x20) = __ptr;
    _ZdlPv(__ptr);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
            (param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~
