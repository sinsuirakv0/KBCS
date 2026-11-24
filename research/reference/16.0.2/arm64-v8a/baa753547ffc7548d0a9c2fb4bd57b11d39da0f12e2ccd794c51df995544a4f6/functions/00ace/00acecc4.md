# 00acecc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acec54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0065.md#compare-6e96ab1f045a37aabe83793aa548a767)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0077.md#compare-2b73b940e45842bb8a8ba65f7dfddceb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acecc4",
  "name": "FUN_00acecc4",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538",
  "source_text_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538"
}
~~~

## 呼び出し元

- [0066242c](../00662/0066242c.md)
- [006624d0](../00662/006624d0.md)
- [00662574](../00662/00662574.md)
- [007ccf44](../007cc/007ccf44.md)
- [007de918](../007de/007de918.md)
- [008c42e4](../008c4/008c42e4.md)
- [00a47f54](../00a47/00a47f54.md)
- [00acc640](../00acc/00acc640.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)
- [00ad09c8](../00ad0/00ad09c8.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00802710](../00802/00802710.md)
- [00aeae8c](../00aea/00aeae8c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

## 疑似コード / UTF-8 2554 bytes

~~~c

uint FUN_00acecc4(long param_1,int param_2)

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
  
                    /* try { // try from 00acecd8 to 00bcece3 has its CatchHandler @ 00acf64c */
                    /* try { // try from 00acece4 to 00bced03 has its CatchHandler @ 00acf5f8 */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar5 = FUN_00802710(0);
                    /* try { // try from 00aced04 to 00bcee53 has its CatchHandler @ 00accbd0 */
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
                    /* try { // try from 00acee54 to 00bcee6f has its CatchHandler @ 00acf5e4 */
                    /* WARNING: Subroutine does not return */
            FUN_00470880(&local_80);
          }
          goto LAB_00acee8c;
        }
        __dest = (void *)_Znwm(__n);
        memcpy(__dest,__src,__n);
        if (pvVar1 != __src) {
          sVar7 = 0;
          do {
            if (*(int *)((long)__dest + sVar7) == param_2) {
              _ZdlPv(__dest);
              uVar6 = 1;
              goto LAB_00acee14;
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
      uVar6 = FUN_00aeae8c(param_1,param_2);
      uVar6 = ~uVar6 >> 0x1f;
      goto LAB_00acee14;
    }
  }
  uVar6 = 0;
LAB_00acee14:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar6;
  }
LAB_00acee8c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
