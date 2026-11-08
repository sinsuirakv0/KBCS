# 00b0cefc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
