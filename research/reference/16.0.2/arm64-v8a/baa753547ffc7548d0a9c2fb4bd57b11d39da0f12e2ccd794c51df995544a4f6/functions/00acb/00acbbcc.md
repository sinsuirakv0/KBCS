# 00acbbcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acbbcc",
  "name": "FUN_00acbbcc",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "466825c0d53e60600d54d8d6a2ea4dc1a77c1d11e1d5eef49511cfe831d3c90d",
  "source_text_sha256": "466825c0d53e60600d54d8d6a2ea4dc1a77c1d11e1d5eef49511cfe831d3c90d"
}
~~~

## 呼び出し元

- [00935b64](../00935/00935b64.md)

## 呼び出し先

- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 1010 bytes

~~~c

void FUN_00acbbcc(long param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  
  lVar5 = tpidr_el0;
  lVar7 = *(long *)(lVar5 + 0x28);
  if (*(char *)(param_1 + 0x28) != '\0') {
    puVar3 = *(undefined8 **)(param_1 + 0x48);
    for (puVar1 = *(undefined8 **)(param_1 + 0x40); puVar1 != puVar3; puVar1 = puVar1 + 2) {
      puVar2 = (undefined8 *)*puVar1;
      plVar4 = (long *)puVar1[1];
      if (plVar4 != (long *)0x0) {
        FUN_00c53d70(1,plVar4 + 1);
      }
      (**(code **)*puVar2)(puVar2,param_2);
      if ((plVar4 != (long *)0x0) &&
         (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)) {
        (**(code **)(*plVar4 + 0x10))(plVar4);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
      }
    }
  }
  if (*(long *)(lVar5 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
