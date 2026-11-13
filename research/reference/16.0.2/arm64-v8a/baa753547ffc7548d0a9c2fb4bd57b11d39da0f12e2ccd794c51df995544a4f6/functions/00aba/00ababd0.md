# 00ababd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00ababd0",
  "name": "FUN_00ababd0",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d",
  "source_text_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d"
}
~~~

## 呼び出し元

- [005fe6ac](../005fe/005fe6ac.md)

## 呼び出し先

- [00851550](../00851/00851550.md)
- [00ab9228](../00ab9/00ab9228.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 2370 bytes

~~~c

void FUN_00ababd0(int param_1,int param_2)

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
  
                    /* try { // try from 00ababe0 to 00bbad53 has its CatchHandler @ 00aba9b0 */
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  if ((param_1 == 3) ||
     (lVar6 = FUN_00851550(), puVar4 = PTR_DAT_00c9b5a0, lVar6 = lVar6 + (long)param_1 * 0x18,
     (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) - *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4
          ) * -0x55555555 < 1)) {
    iVar5 = 0;
  }
  else {
    iVar8 = 0;
    do {
      lVar6 = 0;
      while( true ) {
        lVar7 = FUN_00851550();
                    /* catch() { ... } // from try @ 00ababc8 with catch @ 00abac6c */
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        lVar7 = (long)local_98[0];
        if (local_90 != (void *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
        if (lVar7 <= lVar6) break;
        lVar7 = FUN_00851550();
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        iVar1 = *(int *)(puVar4 + (long)param_2 * 4);
                    /* catch() { ... } // from try @ 00abaaa4 with catch @ 00abacb0 */
        iVar2 = *(int *)((long)local_90 + lVar6 * 4);
        local_88 = local_90;
        _ZdlPv(local_90);
        lVar6 = lVar6 + 1;
        iVar5 = iVar8;
        if (iVar2 == iVar1) goto LAB_00abad14;
      }
                    /* catch() { ... } // from try @ 00abaa80 with catch @ 00abaccc */
      iVar8 = iVar8 + 1;
      lVar6 = FUN_00851550();
                    /* catch() { ... } // from try @ 00abaafc with catch @ 00abacd4 */
      lVar6 = lVar6 + (long)param_1 * 0x18;
                    /* catch() { ... } // from try @ 00ababa8 with catch @ 00abacdc */
                    /* catch() { ... } // from try @ 00abab20 with catch @ 00abace4 */
      iVar5 = 0;
    } while (iVar8 < (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) -
                                  *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4) * -0x55555555);
  }
LAB_00abad14:
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(iVar5);
  }
  return;
}

~~~
