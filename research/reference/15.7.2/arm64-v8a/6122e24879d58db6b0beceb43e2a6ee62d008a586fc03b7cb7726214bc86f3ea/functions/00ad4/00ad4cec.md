# 00ad4cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00ad4cec",
  "name": "FUN_00ad4cec",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acdd189ea8a4bb98ff703b45a57ad3fa025af359354c7f1ecc51eb9559c2f9cc",
  "source_text_sha256": "acdd189ea8a4bb98ff703b45a57ad3fa025af359354c7f1ecc51eb9559c2f9cc"
}
~~~

## 呼び出し元

- [00ad4424](../00ad4/00ad4424.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [0041e380](../0041e/0041e380.md)
- [0041e41c](../0041e/0041e41c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード / UTF-8 2682 bytes

~~~c

ulong * FUN_00ad4cec(long *param_1,char *param_2)

{
  ulong uVar1;
  long lVar2;
  size_t sVar3;
  void *__ptr;
  long lVar4;
  long lVar5;
  long lVar6;
  undefined1 *puVar7;
  ulong *puVar8;
  undefined1 *puVar9;
  void *__dest;
  
  lVar2 = tpidr_el0;
  lVar4 = *(long *)(lVar2 + 0x28);
  lVar5 = param_1[1] - *param_1 >> 3;
  puVar8 = (ulong *)(lVar5 * -0x5555555555555555);
  puVar9 = (undefined1 *)((long)puVar8 + 1);
  if (puVar9 < (undefined1 *)0xaaaaaaaaaaaaaab) {
    lVar6 = param_1[2] - *param_1 >> 3;
    puVar7 = (undefined1 *)(lVar6 * 0x5555555555555556);
    if (puVar7 < puVar9 || (long)puVar7 - (long)puVar9 == 0) {
      puVar7 = puVar9;
    }
    if (0x555555555555554 < (ulong)(lVar6 * -0x5555555555555555)) {
      puVar7 = (undefined1 *)0xaaaaaaaaaaaaaaa;
    }
    if (puVar7 == (undefined1 *)0x0) {
      lVar6 = 0;
    }
    else {
      if ((undefined1 *)0xaaaaaaaaaaaaaaa < puVar7) {
        if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
          FUN_0041e380();
        }
        goto LAB_00ad4ee4;
      }
      lVar6 = _Znwm((long)puVar7 * 0x18);
    }
    puVar8 = (ulong *)(lVar6 + lVar5 * 8);
    sVar3 = strlen(param_2);
    if (sVar3 < 0xfffffffffffffff8) {
      if (sVar3 < 0x17) {
        puVar9 = (undefined1 *)((long)puVar8 + 1);
        *(char *)puVar8 = (char)((int)sVar3 << 1);
        if (sVar3 != 0) goto LAB_00ad4e08;
      }
      else {
        uVar1 = (sVar3 & 0xfffffffffffffff8) + 8;
        if ((sVar3 | 7) != 0x17) {
          uVar1 = sVar3 | 7;
        }
        puVar9 = (undefined1 *)_Znwm(uVar1 + 1);
        puVar8[1] = sVar3;
        puVar8[2] = (ulong)puVar9;
        *puVar8 = uVar1 + 1 | 1;
LAB_00ad4e08:
        memmove(puVar9,param_2,sVar3);
      }
      puVar9[sVar3] = 0;
      sVar3 = param_1[1] - *param_1;
      __dest = (void *)((long)puVar8 - sVar3);
      memcpy(__dest,(void *)*param_1,sVar3);
      __ptr = (void *)*param_1;
      *param_1 = (long)__dest;
      param_1[1] = (long)(puVar8 + 3);
      param_1[2] = lVar6 + (long)puVar7 * 0x18;
      if (__ptr != (void *)0x0) {
        _ZdlPv(__ptr);
      }
      if (*(long *)(lVar2 + 0x28) == lVar4) {
        return puVar8 + 3;
      }
      goto LAB_00ad4ee4;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != lVar4) goto LAB_00ad4ee4;
    FUN_0041e41c(param_1);
  }
                    /* catch() { ... } // from try @ 00ad5078 with catch @ 00ad4e9c */
  if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(puVar8);
  }
LAB_00ad4ee4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
