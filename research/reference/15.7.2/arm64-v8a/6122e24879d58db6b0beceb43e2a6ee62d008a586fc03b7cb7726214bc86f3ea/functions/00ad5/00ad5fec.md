# 00ad5fec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00ad60f8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad6/00ad60f8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00ad5fec",
  "name": "FUN_00ad5fec",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc0b4deb46a094d3b2167dd44da00a4e15521abe59f996d0a4f839b85dc9e2db",
  "source_text_sha256": "dc0b4deb46a094d3b2167dd44da00a4e15521abe59f996d0a4f839b85dc9e2db"
}
~~~

## 呼び出し元

- [00ad5e00](../00ad5/00ad5e00.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

## 疑似コード / UTF-8 1502 bytes

~~~c

long * FUN_00ad5fec(long param_1,undefined8 *param_2,byte *param_3)

{
  void *__s2;
  size_t __n;
  ulong uVar1;
  byte *__s1;
  bool bVar2;
  ulong uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = (long *)(param_1 + 8);
  plVar5 = (long *)*plVar6;
  plVar7 = plVar6;
  if (plVar5 != (long *)0x0) {
    uVar1 = *(ulong *)(param_3 + 8);
    __s1 = *(byte **)(param_3 + 0x10);
    if ((*param_3 & 1) == 0) {
      __s1 = param_3 + 1;
      uVar1 = (ulong)(*param_3 >> 1);
    }
    do {
      while( true ) {
        plVar7 = plVar5;
        __s2 = (void *)((long)plVar7 + 0x21);
        uVar3 = (ulong)(*(byte *)(plVar7 + 4) >> 1);
        if ((*(byte *)(plVar7 + 4) & 1) != 0) {
          __s2 = (void *)plVar7[6];
          uVar3 = plVar7[5];
        }
        __n = uVar3;
        if (uVar1 <= uVar3) {
          __n = uVar1;
        }
        iVar4 = memcmp(__s1,__s2,__n);
        bVar2 = uVar1 < uVar3;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (bVar2) break;
        iVar4 = memcmp(__s2,__s1,__n);
        bVar2 = uVar3 < uVar1;
        if (iVar4 != 0) {
          bVar2 = iVar4 < 0;
        }
        if (!bVar2) goto LAB_00ad60d0;
        plVar6 = plVar7 + 1;
        plVar5 = (long *)*plVar6;
        if ((long *)*plVar6 == (long *)0x0) goto LAB_00ad60d0;
      }
      plVar5 = (long *)*plVar7;
      plVar6 = plVar7;
    } while ((long *)*plVar7 != (long *)0x0);
  }
LAB_00ad60d0:
  *param_2 = plVar7;
  return plVar6;
}

~~~
