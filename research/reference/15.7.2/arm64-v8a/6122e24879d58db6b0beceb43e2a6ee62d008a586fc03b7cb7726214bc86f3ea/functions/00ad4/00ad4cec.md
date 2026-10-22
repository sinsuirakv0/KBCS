# 00ad4cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ad4cec.md)

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
  "source_sha256": "81a05aa239796f0134a72ab56000c9ec05db6ddad1680e8f8dbeb9dac6534ecc",
  "source_text_sha256": "81a05aa239796f0134a72ab56000c9ec05db6ddad1680e8f8dbeb9dac6534ecc"
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

## 疑似コード 1/1 / UTF-8 2864 bytes

~~~c

ulong * FUN_00ad4cec(long *param_1,char *param_2)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  size_t sVar4;
  void *pvVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  undefined1 *puVar9;
  ulong *puVar10;
  undefined1 *puVar11;
  void *__dest;
  
  lVar2 = tpidr_el0;
  lVar6 = *(long *)(lVar2 + 0x28);
  lVar7 = param_1[1] - *param_1 >> 3;
  puVar10 = (ulong *)(lVar7 * -0x5555555555555555);
  puVar11 = (undefined1 *)((long)puVar10 + 1);
  if (puVar11 < (undefined1 *)0xaaaaaaaaaaaaaab) {
    lVar8 = param_1[2] - *param_1 >> 3;
    puVar9 = (undefined1 *)(lVar8 * 0x5555555555555556);
    if (puVar9 < puVar11 || (long)puVar9 - (long)puVar11 == 0) {
      puVar9 = puVar11;
    }
    if (0x555555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      puVar9 = (undefined1 *)0xaaaaaaaaaaaaaaa;
    }
    if (puVar9 == (undefined1 *)0x0) {
      pvVar3 = (void *)0x0;
    }
    else {
      if ((undefined1 *)0xaaaaaaaaaaaaaaa < puVar9) {
        if (*(long *)(lVar2 + 0x28) == lVar6) {
                    /* WARNING: Subroutine does not return */
          FUN_0041e380();
        }
        goto LAB_00ad4ee4;
      }
      pvVar3 = operator_new((long)puVar9 * 0x18);
    }
    puVar10 = (ulong *)((long)pvVar3 + lVar7 * 8);
    sVar4 = strlen(param_2);
    if (sVar4 < 0xfffffffffffffff8) {
      if (sVar4 < 0x17) {
        puVar11 = (undefined1 *)((long)puVar10 + 1);
        *(char *)puVar10 = (char)((int)sVar4 << 1);
        if (sVar4 != 0) goto LAB_00ad4e08;
      }
      else {
        uVar1 = (sVar4 & 0xfffffffffffffff8) + 8;
        if ((sVar4 | 7) != 0x17) {
          uVar1 = sVar4 | 7;
        }
        puVar11 = operator_new(uVar1 + 1);
        puVar10[1] = sVar4;
        puVar10[2] = (ulong)puVar11;
        *puVar10 = uVar1 + 1 | 1;
LAB_00ad4e08:
        memmove(puVar11,param_2,sVar4);
      }
      puVar11[sVar4] = 0;
      sVar4 = param_1[1] - *param_1;
      __dest = (void *)((long)puVar10 - sVar4);
      memcpy(__dest,(void *)*param_1,sVar4);
      pvVar5 = (void *)*param_1;
      *param_1 = (long)__dest;
      param_1[1] = (long)(puVar10 + 3);
      param_1[2] = (long)((long)pvVar3 + (long)puVar9 * 0x18);
      if (pvVar5 != (void *)0x0) {
        operator_delete(pvVar5);
      }
      if (*(long *)(lVar2 + 0x28) == lVar6) {
        return puVar10 + 3;
      }
      goto LAB_00ad4ee4;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != lVar6) goto LAB_00ad4ee4;
    FUN_0041e41c(param_1);
  }
                    /* catch() { ... } // from try @ 00ad5078 with catch @ 00ad4e9c */
  if (*(long *)(lVar2 + 0x28) == lVar6) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(puVar10);
  }
LAB_00ad4ee4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
