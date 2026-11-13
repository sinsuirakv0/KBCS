# 00b6ddfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
