# 00b8cbfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b8cbfc",
  "name": "_ZN11flatbuffers6Parser9ParseJsonEPKcS2_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1bf799f9182e74f9225b118092238d4aaa23ca21d417ee77a0373d058baa623",
  "source_text_sha256": "b1bf799f9182e74f9225b118092238d4aaa23ca21d417ee77a0373d058baa623"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5cab0](../00c5c/00c5cab0.md)
- [00c5d550](../00c5d/00c5d550.md)
- [00c5d650](../00c5d/00c5d650.md)

## 疑似コード / UTF-8 2028 bytes

~~~c

void _ZN11flatbuffers6Parser9ParseJsonEPKcS2_(long param_1,undefined8 param_2,undefined8 param_3)

{
  uint uVar1;
  long lVar2;
  bool bVar3;
  long lVar4;
  long lVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  char local_68 [8];
  char local_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  uVar1 = *(uint *)(param_1 + 0x1a8);
  lVar4 = *(long *)(param_1 + 400);
  *(undefined4 *)(param_1 + 0x1a8) = 0;
  *(undefined2 *)(param_1 + 0x1ac) = 0;
  *(ulong *)(param_1 + 0x1a0) = *(long *)(param_1 + 0x1a0) + (ulong)uVar1 * -8;
  if (lVar4 == 0) {
    lVar5 = 0;
    *(undefined8 *)(param_1 + 0x180) = 0;
  }
  else {
    lVar5 = lVar4 + *(long *)(param_1 + 0x180);
  }
  puVar6 = *(undefined8 **)(param_1 + 0x1d0);
  *(undefined4 *)(param_1 + 0x188) = 0;
  *(long *)(param_1 + 0x198) = lVar5;
  *(long *)(param_1 + 0x1a0) = lVar4;
  *(undefined2 *)(param_1 + 0x1b8) = 0;
  *(undefined8 *)(param_1 + 0x1c0) = 1;
  *(undefined8 *)(param_1 + 0x1b0) = 0;
  if (puVar6 != (undefined8 *)0x0) {
    puVar7 = puVar6 + 1;
    _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (puVar6,*puVar7);
    *puVar6 = puVar7;
    puVar6[2] = 0;
    *puVar7 = 0;
  }
  _ZN11flatbuffers6Parser14StartParseFileEPKcS2_(local_60,param_1,param_2,param_3);
  local_60[1] = 1;
  if (local_60[0] == '\0') {
    _ZN11flatbuffers6Parser11DoParseJsonEv(local_68,param_1);
    bVar3 = local_68[0] == '\0';
  }
  else {
                    /* try { // try from 00b8ccc0 to 00c8cce7 has its CatchHandler @ 00b8eadc */
    bVar3 = false;
  }
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* try { // try from 00b8ccf4 to 00c8ccfb has its CatchHandler @ 00b8ead4 */
                    /* try { // try from 00b8cd00 to 00c8cd17 has its CatchHandler @ 00b8eacc */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(bVar3);
}

~~~
