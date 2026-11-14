# 00abbbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abbbc4",
  "name": "FUN_00abbbc4",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e024db009c5aa530f8fe630be4a5dfed593c69a82a63a309c71ff2067589e1e5",
  "source_text_sha256": "e024db009c5aa530f8fe630be4a5dfed593c69a82a63a309c71ff2067589e1e5"
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [00aba21c](../00aba/00aba21c.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 3400 bytes

~~~c

void FUN_00abbbc4(int param_1,int param_2)

{
  int iVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  int iVar8;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00abbb74 with catch @ 00abbc18 */
  if ((param_1 == 3) ||
     (lVar6 = FUN_008524fc(), puVar4 = PTR_DAT_00c9c570, lVar6 = lVar6 + (long)param_1 * 0x18,
     (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) - *(long *)((long)&uleb128_0029a6e0 + lVar6)
                  ) >> 4) * -0x55555555 < 1)) {
    iVar5 = 0;
                    /* catch() { ... } // from try @ 00abbe50 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc070 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc1f0 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc364 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc4b8 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc5b4 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc864 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc954 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abca44 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abcc78 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abce0c with catch @ 00abbd00
                       catch() { ... } // from try @ 00abced4 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abcf8c with catch @ 00abbd00 */
  }
  else {
    iVar8 = 0;
    do {
      lVar6 = 0;
      while( true ) {
        lVar7 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00abba50 with catch @ 00abbc5c */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        lVar7 = (long)local_98[0];
        if (local_90 != (void *)0x0) {
          local_88 = local_90;
                    /* catch() { ... } // from try @ 00abba2c with catch @ 00abbc78 */
          _ZdlPv(local_90);
        }
                    /* catch() { ... } // from try @ 00abbaa8 with catch @ 00abbc80 */
        if (lVar7 <= lVar6) break;
        lVar7 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00abbb54 with catch @ 00abbc88 */
                    /* catch() { ... } // from try @ 00abbacc with catch @ 00abbc90 */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        iVar1 = *(int *)(puVar4 + (long)param_2 * 4);
        iVar2 = *(int *)((long)local_90 + lVar6 * 4);
        local_88 = local_90;
        _ZdlPv(local_90);
        lVar6 = lVar6 + 1;
        iVar5 = iVar8;
        if (iVar2 == iVar1) goto LAB_00abbd08;
      }
      iVar8 = iVar8 + 1;
      lVar6 = FUN_008524fc();
      lVar6 = lVar6 + (long)param_1 * 0x18;
      iVar5 = 0;
    } while (iVar8 < (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) -
                                  *(long *)((long)&uleb128_0029a6e0 + lVar6)) >> 4) * -0x55555555);
  }
LAB_00abbd08:
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(iVar5);
  }
  return;
}

~~~
