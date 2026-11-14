# 00acfcb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acfcb8",
  "name": "FUN_00acfcb8",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eac2ab26bdba2150fc189f5005ecb5567dd68ff48dabb818ffeac94f73d6f1bc",
  "source_text_sha256": "eac2ab26bdba2150fc189f5005ecb5567dd68ff48dabb818ffeac94f73d6f1bc"
}
~~~

## 呼び出し元

- [006627dc](../00662/006627dc.md)
- [00662880](../00662/00662880.md)
- [00662924](../00662/00662924.md)
- [007cdea8](../007cd/007cdea8.md)
- [007df87c](../007df/007df87c.md)
- [008c5290](../008c5/008c5290.md)
- [00a48f48](../00a48/00a48f48.md)
- [00acd634](../00acd/00acd634.md)
- [00acfe84](../00acf/00acfe84.md)
- [00ad021c](../00ad0/00ad021c.md)
- [00ad19bc](../00ad1/00ad19bc.md)

## 呼び出し先

- [00470ba0](../00470/00470ba0.md)
- [00803674](../00803/00803674.md)
- [00aebe80](../00aeb/00aebe80.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)

## 疑似コード / UTF-8 2360 bytes

~~~c

uint FUN_00acfcb8(long param_1,int param_2)

{
  void *__src;
  void *pvVar1;
  size_t __n;
  long lVar2;
  long *plVar3;
  bool bVar4;
  int iVar5;
  uint uVar6;
  void *__dest;
  size_t sVar7;
  long *plVar8;
  long *plVar9;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar5 = FUN_00803674(0);
  if ((0x13 < iVar5 + 0x19U) || ((0x87c01U >> (ulong)(iVar5 + 0x19U & 0x1f) & 1) == 0)) {
    plVar8 = *(long **)(param_1 + 0x33c0);
    while (plVar8 != (long *)(param_1 + 0x33c8)) {
      __src = (void *)plVar8[5];
      pvVar1 = (void *)plVar8[6];
      local_78 = 0;
      uStack_70 = 0;
      __n = (long)pvVar1 - (long)__src;
      local_80 = 0;
      if (__n != 0) {
        if ((long)__n < 0) {
          if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470ba0(&local_80);
          }
          goto LAB_00acfe80;
        }
        __dest = (void *)_Znwm(__n);
        memcpy(__dest,__src,__n);
        if (pvVar1 != __src) {
          sVar7 = 0;
          do {
            if (*(int *)((long)__dest + sVar7) == param_2) {
              _ZdlPv(__dest);
              uVar6 = 1;
              goto LAB_00acfe08;
            }
            sVar7 = sVar7 + 4;
          } while (__n != sVar7);
        }
        _ZdlPv(__dest);
      }
      plVar3 = (long *)plVar8[1];
      plVar9 = plVar8;
      if ((long *)plVar8[1] == (long *)0x0) {
        do {
          plVar8 = (long *)plVar9[2];
          bVar4 = (long *)*plVar8 != plVar9;
          plVar9 = plVar8;
        } while (bVar4);
      }
      else {
        do {
          plVar8 = plVar3;
          plVar3 = (long *)*plVar8;
        } while ((long *)*plVar8 != (long *)0x0);
      }
    }
    if (999999999 < param_2) {
      uVar6 = FUN_00aebe80(param_1,param_2);
      uVar6 = ~uVar6 >> 0x1f;
                    /* try { // try from 00acfe00 to 00bcfe1b has its CatchHandler @ 00ad0590 */
      goto LAB_00acfe08;
    }
  }
  uVar6 = 0;
LAB_00acfe08:
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00acfe1c to 00bd09f3 has its CatchHandler @ 00acdb7c */
    return uVar6;
  }
LAB_00acfe80:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
