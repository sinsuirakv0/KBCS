# 00b6eebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b6eebc",
  "name": "_ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60055d8fc72005b7b2657688e98233b50b2a5e5637cc50e5c543fd220e0b8e14",
  "source_text_sha256": "60055d8fc72005b7b2657688e98233b50b2a5e5637cc50e5c543fd220e0b8e14"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0054a5d4](../0054a/0054a5d4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5b1b0](../00c5b/00c5b1b0.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)

## 疑似コード / UTF-8 1268 bytes

~~~c

undefined8 *
_ZNK11flatbuffers6Parser15GetPooledStringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
          (long param_1,undefined8 param_2)

{
  long *plVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  plVar1 = (long *)(param_1 + 0x5c8);
  puVar3 = (undefined8 *)FUN_0054a5d4(plVar1,&local_50,param_2);
  puVar5 = (undefined8 *)*puVar3;
  if (puVar5 == (undefined8 *)0x0) {
    puVar5 = (undefined8 *)_Znwm(0x38);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(puVar5 + 4,param_2);
    *puVar5 = 0;
    puVar5[1] = 0;
    puVar5[2] = local_50;
    *puVar3 = puVar5;
    puVar4 = puVar5;
    if (*(long *)*plVar1 != 0) {
      *plVar1 = *(long *)*plVar1;
      puVar4 = (undefined8 *)*puVar3;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
              (*(undefined8 *)(param_1 + 0x5d0),puVar4);
    *(long *)(param_1 + 0x5d8) = *(long *)(param_1 + 0x5d8) + 1;
  }
  if (*(long *)(lVar2 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return puVar5 + 4;
}

~~~
