# 007bbbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007bbbec",
  "name": "FUN_007bbbec",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "589f7514852d7414548427c155f2f7446517e1d2d39839419cdd2341af6ba70a",
  "source_text_sha256": "589f7514852d7414548427c155f2f7446517e1d2d39839419cdd2341af6ba70a"
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [006bed1c](../006be/006bed1c.md)
- [007bda04](../007bd/007bda04.md)
- [007df0a8](../007df/007df0a8.md)
- [00802678](../00802/00802678.md)
- [00933edc](../00933/00933edc.md)
- [009d9790](../009d9/009d9790.md)
- [00a47d08](../00a47/00a47d08.md)
- [00afdfe4](../00afd/00afdfe4.md)
- [00aff204](../00aff/00aff204.md)

## 呼び出し先

- [0080018c](../00800/0080018c.md)
- [00802ea0](../00802/00802ea0.md)
- [008077b8](../00807/008077b8.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 1035 bytes

~~~c

undefined8 FUN_007bbbec(long param_1)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  undefined8 uVar4;
  
  lVar2 = FUN_008514b8();
  iVar1 = FUN_0080018c(*(undefined4 *)(BYTE_ARRAY_0038f27d + lVar2 + 7));
  if ((((iVar1 == 0) && (*(int *)((long)&QWORD_00344440 + param_1) == 0x30)) &&
      (iVar1 = FUN_00802ea0(), iVar1 == 3)) &&
     ((uVar3 = FUN_008077b8(0,0x30,3,0), (uVar3 & 1) != 0 && (*(char *)(param_1 + 0x15a0) == '\0')))
     ) {
    uVar4 = 1;
  }
  else {
                    /* try { // try from 007bbc58 to 008bbe6b has its CatchHandler @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bbc58 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bbeb4 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007bcdd0 with catch @ 007bbc58
                       catch(type#1 @ 00000000) { ... } // from try @ 007be150 with catch @ 007bbc58
                        */
    uVar4 = 0;
  }
  return uVar4;
}

~~~
