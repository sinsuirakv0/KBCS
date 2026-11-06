# 00ad4bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00ad4bfc.md)

## 関数情報

~~~json
{
  "address": "00ad4bfc",
  "name": "FUN_00ad4bfc",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23eb56be9696d36e081c3578986f27b2c6129ef858b53af6d8040bb57409ea7c",
  "source_text_sha256": "23eb56be9696d36e081c3578986f27b2c6129ef858b53af6d8040bb57409ea7c"
}
~~~
## 呼び出し元

- [00ad4530](../00ad4/00ad4530.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [0041e380](../0041e/0041e380.md)
- [0041e41c](../0041e/0041e41c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

## 疑似コード 1/1 / UTF-8 2595 bytes

~~~c

ulong * FUN_00ad4bfc(long *param_1,char *param_2)

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
        goto LAB_00ad4df4;
      }
      lVar6 = _Znwm((long)puVar7 * 0x18);
    }
    puVar8 = (ulong *)(lVar6 + lVar5 * 8);
    sVar3 = strlen(param_2);
    if (sVar3 < 0xfffffffffffffff8) {
      if (sVar3 < 0x17) {
        puVar9 = (undefined1 *)((long)puVar8 + 1);
        *(char *)puVar8 = (char)((int)sVar3 << 1);
        if (sVar3 != 0) goto LAB_00ad4d18;
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
LAB_00ad4d18:
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
      goto LAB_00ad4df4;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != lVar4) goto LAB_00ad4df4;
    FUN_0041e41c(param_1);
  }
  if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(puVar8);
  }
LAB_00ad4df4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
