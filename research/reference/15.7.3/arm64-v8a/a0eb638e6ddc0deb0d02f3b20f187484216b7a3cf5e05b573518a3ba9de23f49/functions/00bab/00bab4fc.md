# 00bab4fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bab434`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab434.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-97e2a5bfcfd44d056c4d5e62ace605ab)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bab540`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab540.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-eeeca747c5790ab81efd930bcb5fc88c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab4fc",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_",
  "size": 668,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "31cb74985d58b875f3df37e6341c9102894a3fa943baaae52575e0e7dff5f013",
  "source_text_sha256": "31cb74985d58b875f3df37e6341c9102894a3fa943baaae52575e0e7dff5f013",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bab4fc",
        "00bab797"
      ]
    ],
    "bytes_sha256": "dd9237fcc7392abb5808e2bea1c30bd57f2799b5dc158b288715ee2ced4c4bb6",
    "instruction_count": 167,
    "instruction_bytes": 668,
    "body_bytes": 668,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1530](../00be1/00be1530.md)
- [00be1af0](../00be1/00be1af0.md)
- [00be1b00](../00be1/00be1b00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3426 bytes

~~~c

undefined1
_ZNKSt6__ndk17codecvtIwc9mbstate_tE6do_outERS1_PKwS5_RS5_PcS7_RS7_
          (long param_1,mbstate_t *param_2,wchar_t *param_3,wchar_t *param_4,wchar_t **param_5,
          char *param_6,char *param_7,long *param_8)

{
  wchar_t *pwVar1;
  wchar_t __wc;
  char cVar2;
  __locale_t p_Var3;
  size_t sVar4;
  char *pcVar5;
  char *pcVar6;
  wchar_t *pwVar7;
  char acStack_74 [4];
  mbstate_t local_70;
  __locale_t local_68;
  
  pwVar7 = param_3;
  for (pwVar1 = param_3; (pwVar1 != param_4 && (pwVar7 = pwVar1, *pwVar1 != L'\0'));
      pwVar1 = pwVar1 + 1) {
    pwVar7 = param_4;
  }
  *param_8 = (long)param_6;
  *param_5 = param_3;
  while( true ) {
    if ((param_3 == param_4) || (param_6 == param_7)) goto LAB_00bab764;
    local_70 = *param_2;
    p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
    local_68 = p_Var3;
    sVar4 = wcsnrtombs(param_6,param_5,(long)pwVar7 - (long)param_3 >> 2,
                       (long)param_7 - (long)param_6,param_2);
    if (p_Var3 != (__locale_t)0x0) {
      uselocale(p_Var3);
    }
    if (sVar4 == 0) {
      return true;
    }
    if (sVar4 == 0xffffffffffffffff) {
      *param_8 = (long)param_6;
      if (param_3 == *param_5) goto LAB_00bab74c;
      goto LAB_00bab6ec;
    }
    param_6 = (char *)(*param_8 + sVar4);
    *param_8 = (long)param_6;
    if (param_6 == param_7) break;
    if (pwVar7 == param_4) {
      param_3 = *param_5;
      pwVar7 = param_4;
    }
    else {
      p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
      local_68 = p_Var3;
      sVar4 = wcrtomb(acStack_74,L'\0',param_2);
      if (p_Var3 != (__locale_t)0x0) {
        uselocale(p_Var3);
      }
      if (sVar4 == 0xffffffffffffffff) {
        return 2;
      }
      if ((ulong)((long)param_7 - *param_8) < sVar4) {
        return true;
      }
      if (sVar4 != 0) {
        pcVar5 = acStack_74;
        do {
          pcVar6 = (char *)*param_8;
          cVar2 = *pcVar5;
          sVar4 = sVar4 - 1;
          *param_8 = (long)(pcVar6 + 1);
          *pcVar6 = cVar2;
          pcVar5 = pcVar5 + 1;
        } while (sVar4 != 0);
      }
      param_3 = *param_5 + 1;
      *param_5 = param_3;
      for (pwVar1 = param_3;
          (pwVar7 = param_4, pwVar1 != param_4 && (pwVar7 = pwVar1, *pwVar1 != L'\0'));
          pwVar1 = pwVar1 + 1) {
      }
      param_6 = (char *)*param_8;
    }
  }
  param_3 = *param_5;
LAB_00bab764:
  return param_3 != param_4;
  while( true ) {
    param_3 = param_3 + 1;
    param_6 = (char *)(*param_8 + sVar4);
    *param_8 = (long)param_6;
                    /* try { // try from 00bab744 to 00cab7bb has its CatchHandler @ 00bab744
                       catch() { ... } // from try @ 00bab744 with catch @ 00bab744
                       catch() { ... } // from try @ 00bab85c with catch @ 00bab744
                       catch() { ... } // from try @ 00bab9ac with catch @ 00bab744
                       catch() { ... } // from try @ 00babb2c with catch @ 00bab744
                       catch() { ... } // from try @ 00babc48 with catch @ 00bab744 */
    if (param_3 == *param_5) break;
LAB_00bab6ec:
    __wc = *param_3;
    p_Var3 = uselocale(*(__locale_t *)(param_1 + 0x10));
    local_68 = p_Var3;
    sVar4 = wcrtomb(param_6,__wc,&local_70);
    if (p_Var3 != (__locale_t)0x0) {
      uselocale(p_Var3);
    }
    if (sVar4 == 0xffffffffffffffff) break;
  }
LAB_00bab74c:
  *param_5 = param_3;
  return 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bab4fc"></a> `00bab4fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bab500"></a> `00bab500` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bab504"></a> `00bab504` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab508"></a> `00bab508` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab50c"></a> `00bab50c` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab510"></a> `00bab510` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bab514"></a> `00bab514` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bab518"></a> `00bab518` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bab51c"></a> `00bab51c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bab520"></a> `00bab520` | `f4 03 07 aa` | mov x20,x7 | `FALL_THROUGH`
<a id="insn-00bab524"></a> `00bab524` | `f7 03 06 aa` | mov x23,x6 | `FALL_THROUGH`
<a id="insn-00bab528"></a> `00bab528` | `fa 03 05 aa` | mov x26,x5 | `FALL_THROUGH`
<a id="insn-00bab52c"></a> `00bab52c` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bab530"></a> `00bab530` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bab534"></a> `00bab534` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00bab538"></a> `00bab538` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bab53c"></a> `00bab53c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bab540"></a> `00bab540` | `e0 93 00 a9` | stp x0,x4,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab544"></a> `00bab544` | `00 01 00 54` | b.eq 0x00bab564 | `CONDITIONAL_JUMP`
<a id="insn-00bab548"></a> `00bab548` | `f6 03 18 aa` | mov x22,x24 | `FALL_THROUGH`
<a id="insn-00bab54c"></a> `00bab54c` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00bab550"></a> `00bab550` | `a8 00 00 34` | cbz w8,0x00bab564 | `CONDITIONAL_JUMP`
<a id="insn-00bab554"></a> `00bab554` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bab558"></a> `00bab558` | `df 02 13 eb` | cmp x22,x19 | `FALL_THROUGH`
<a id="insn-00bab55c"></a> `00bab55c` | `81 ff ff 54` | b.ne 0x00bab54c | `CONDITIONAL_JUMP`
<a id="insn-00bab560"></a> `00bab560` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00bab564"></a> `00bab564` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab568"></a> `00bab568` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-00bab56c"></a> `00bab56c` | `9a 02 00 f9` | str x26,[x20] | `FALL_THROUGH`
<a id="insn-00bab570"></a> `00bab570` | `18 01 00 f9` | str x24,[x8] | `FALL_THROUGH`
<a id="insn-00bab574"></a> `00bab574` | `c1 00 00 54` | b.ne 0x00bab58c | `CONDITIONAL_JUMP`
<a id="insn-00bab578"></a> `00bab578` | `7b 00 00 14` | b 0x00bab764 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab57c"></a> `00bab57c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bab580"></a> `00bab580` | `9a 02 40 f9` | ldr x26,[x20] | `FALL_THROUGH`
<a id="insn-00bab584"></a> `00bab584` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-00bab588"></a> `00bab588` | `e0 0e 00 54` | b.eq 0x00bab764 | `CONDITIONAL_JUMP`
<a id="insn-00bab58c"></a> `00bab58c` | `5f 03 17 eb` | cmp x26,x23 | `FALL_THROUGH`
<a id="insn-00bab590"></a> `00bab590` | `a0 0e 00 54` | b.eq 0x00bab764 | `CONDITIONAL_JUMP`
<a id="insn-00bab594"></a> `00bab594` | `c9 02 18 cb` | sub x9,x22,x24 | `FALL_THROUGH`
<a id="insn-00bab598"></a> `00bab598` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00bab59c"></a> `00bab59c` | `f5 02 1a cb` | sub x21,x23,x26 | `FALL_THROUGH`
<a id="insn-00bab5a0"></a> `00bab5a0` | `3b fd 42 93` | asr x27,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bab5a4"></a> `00bab5a4` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab5a8"></a> `00bab5a8` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bab5ac"></a> `00bab5ac` | `20 09 40 f9` | ldr x0,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bab5b0"></a> `00bab5b0` | `e0 d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab5b4"></a> `00bab5b4` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00bab5b8"></a> `00bab5b8` | `a0 83 1f f8` | stur x0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bab5bc"></a> `00bab5bc` | `e1 0b 40 f9` | ldr x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab5c0"></a> `00bab5c0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bab5c4"></a> `00bab5c4` | `e2 03 1b aa` | mov x2,x27 | `FALL_THROUGH`
<a id="insn-00bab5c8"></a> `00bab5c8` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bab5cc"></a> `00bab5cc` | `e4 03 19 aa` | mov x4,x25 | `FALL_THROUGH`
<a id="insn-00bab5d0"></a> `00bab5d0` | `48 d9 00 94` | bl 0x00be1af0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab5d4"></a> `00bab5d4` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bab5d8"></a> `00bab5d8` | `7c 00 00 b4` | cbz x28,0x00bab5e4 | `CONDITIONAL_JUMP`
<a id="insn-00bab5dc"></a> `00bab5dc` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bab5e0"></a> `00bab5e0` | `d4 d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab5e4"></a> `00bab5e4` | `7b 07 00 b4` | cbz x27,0x00bab6d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab5e8"></a> `00bab5e8` | `7f 07 00 b1` | cmn x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bab5ec"></a> `00bab5ec` | `60 07 00 54` | b.eq 0x00bab6d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab5f0"></a> `00bab5f0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bab5f4"></a> `00bab5f4` | `1a 01 1b 8b` | add x26,x8,x27 | `FALL_THROUGH`
<a id="insn-00bab5f8"></a> `00bab5f8` | `5f 03 17 eb` | cmp x26,x23 | `FALL_THROUGH`
<a id="insn-00bab5fc"></a> `00bab5fc` | `9a 02 00 f9` | str x26,[x20] | `FALL_THROUGH`
<a id="insn-00bab600"></a> `00bab600` | `e0 0a 00 54` | b.eq 0x00bab75c | `CONDITIONAL_JUMP`
<a id="insn-00bab604"></a> `00bab604` | `df 02 13 eb` | cmp x22,x19 | `FALL_THROUGH`
<a id="insn-00bab608"></a> `00bab608` | `80 05 00 54` | b.eq 0x00bab6b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab60c"></a> `00bab60c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab610"></a> `00bab610` | `00 09 40 f9` | ldr x0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bab614"></a> `00bab614` | `c7 d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab618"></a> `00bab618` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bab61c"></a> `00bab61c` | `a0 83 1f f8` | stur x0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bab620"></a> `00bab620` | `a0 53 00 d1` | sub x0,x29,#0x14 | `FALL_THROUGH`
<a id="insn-00bab624"></a> `00bab624` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bab628"></a> `00bab628` | `e2 03 19 aa` | mov x2,x25 | `FALL_THROUGH`
<a id="insn-00bab62c"></a> `00bab62c` | `35 d9 00 94` | bl 0x00be1b00 | `UNCONDITIONAL_CALL`
<a id="insn-00bab630"></a> `00bab630` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bab634"></a> `00bab634` | `7a 00 00 b4` | cbz x26,0x00bab640 | `CONDITIONAL_JUMP`
<a id="insn-00bab638"></a> `00bab638` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bab63c"></a> `00bab63c` | `bd d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab640"></a> `00bab640` | `1f 07 00 b1` | cmn x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bab644"></a> `00bab644` | `60 0a 00 54` | b.eq 0x00bab790 | `CONDITIONAL_JUMP`
<a id="insn-00bab648"></a> `00bab648` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bab64c"></a> `00bab64c` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00bab650"></a> `00bab650` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bab654"></a> `00bab654` | `e8 03 00 54` | b.hi 0x00bab6d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab658"></a> `00bab658` | `38 01 00 b4` | cbz x24,0x00bab67c | `CONDITIONAL_JUMP`
<a id="insn-00bab65c"></a> `00bab65c` | `a8 53 00 d1` | sub x8,x29,#0x14 | `FALL_THROUGH`
<a id="insn-00bab660"></a> `00bab660` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bab664"></a> `00bab664` | `0a 15 40 38` | ldrb w10,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bab668"></a> `00bab668` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bab66c"></a> `00bab66c` | `2b 05 00 91` | add x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bab670"></a> `00bab670` | `8b 02 00 f9` | str x11,[x20] | `FALL_THROUGH`
<a id="insn-00bab674"></a> `00bab674` | `2a 01 00 39` | strb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bab678"></a> `00bab678` | `41 ff ff 54` | b.ne 0x00bab660 | `CONDITIONAL_JUMP`
<a id="insn-00bab67c"></a> `00bab67c` | `e9 0b 40 f9` | ldr x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab680"></a> `00bab680` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00bab684"></a> `00bab684` | `28 01 40 f9` | ldr x8,[x9] | `FALL_THROUGH`
<a id="insn-00bab688"></a> `00bab688` | `18 11 00 91` | add x24,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bab68c"></a> `00bab68c` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-00bab690"></a> `00bab690` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00bab694"></a> `00bab694` | `38 01 00 f9` | str x24,[x9] | `FALL_THROUGH`
<a id="insn-00bab698"></a> `00bab698` | `40 f7 ff 54` | b.eq 0x00bab580 | `CONDITIONAL_JUMP`
<a id="insn-00bab69c"></a> `00bab69c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bab6a0"></a> `00bab6a0` | `e9 f6 ff 34` | cbz w9,0x00bab57c | `CONDITIONAL_JUMP`
<a id="insn-00bab6a4"></a> `00bab6a4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bab6a8"></a> `00bab6a8` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bab6ac"></a> `00bab6ac` | `81 ff ff 54` | b.ne 0x00bab69c | `CONDITIONAL_JUMP`
<a id="insn-00bab6b0"></a> `00bab6b0` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00bab6b4"></a> `00bab6b4` | `b3 ff ff 17` | b 0x00bab580 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6b8"></a> `00bab6b8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab6bc"></a> `00bab6bc` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00bab6c0"></a> `00bab6c0` | `18 01 40 f9` | ldr x24,[x8] | `FALL_THROUGH`
<a id="insn-00bab6c4"></a> `00bab6c4` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-00bab6c8"></a> `00bab6c8` | `21 f6 ff 54` | b.ne 0x00bab58c | `CONDITIONAL_JUMP`
<a id="insn-00bab6cc"></a> `00bab6cc` | `26 00 00 14` | b 0x00bab764 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6d0"></a> `00bab6d0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bab6d4"></a> `00bab6d4` | `26 00 00 14` | b 0x00bab76c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6d8"></a> `00bab6d8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab6dc"></a> `00bab6dc` | `9a 02 00 f9` | str x26,[x20] | `FALL_THROUGH`
<a id="insn-00bab6e0"></a> `00bab6e0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab6e4"></a> `00bab6e4` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bab6e8"></a> `00bab6e8` | `20 03 00 54` | b.eq 0x00bab74c | `CONDITIONAL_JUMP`
<a id="insn-00bab6ec"></a> `00bab6ec` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab6f0"></a> `00bab6f0` | `15 03 40 b9` | ldr w21,[x24] | `FALL_THROUGH`
<a id="insn-00bab6f4"></a> `00bab6f4` | `00 09 40 f9` | ldr x0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bab6f8"></a> `00bab6f8` | `8e d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab6fc"></a> `00bab6fc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bab700"></a> `00bab700` | `a0 83 1f f8` | stur x0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bab704"></a> `00bab704` | `a2 43 00 d1` | sub x2,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bab708"></a> `00bab708` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bab70c"></a> `00bab70c` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00bab710"></a> `00bab710` | `fc d8 00 94` | bl 0x00be1b00 | `UNCONDITIONAL_CALL`
<a id="insn-00bab714"></a> `00bab714` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bab718"></a> `00bab718` | `76 00 00 b4` | cbz x22,0x00bab724 | `CONDITIONAL_JUMP`
<a id="insn-00bab71c"></a> `00bab71c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bab720"></a> `00bab720` | `84 d7 00 94` | bl 0x00be1530 | `UNCONDITIONAL_CALL`
<a id="insn-00bab724"></a> `00bab724` | `ff 06 00 b1` | cmn x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bab728"></a> `00bab728` | `20 01 00 54` | b.eq 0x00bab74c | `CONDITIONAL_JUMP`
<a id="insn-00bab72c"></a> `00bab72c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bab730"></a> `00bab730` | `18 13 00 91` | add x24,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00bab734"></a> `00bab734` | `1a 01 17 8b` | add x26,x8,x23 | `FALL_THROUGH`
<a id="insn-00bab738"></a> `00bab738` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab73c"></a> `00bab73c` | `9a 02 00 f9` | str x26,[x20] | `FALL_THROUGH`
<a id="insn-00bab740"></a> `00bab740` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab744"></a> `00bab744` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bab748"></a> `00bab748` | `21 fd ff 54` | b.ne 0x00bab6ec | `CONDITIONAL_JUMP`
<a id="insn-00bab74c"></a> `00bab74c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab750"></a> `00bab750` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bab754"></a> `00bab754` | `18 01 00 f9` | str x24,[x8] | `FALL_THROUGH`
<a id="insn-00bab758"></a> `00bab758` | `05 00 00 14` | b 0x00bab76c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab75c"></a> `00bab75c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab760"></a> `00bab760` | `18 01 40 f9` | ldr x24,[x8] | `FALL_THROUGH`
<a id="insn-00bab764"></a> `00bab764` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-00bab768"></a> `00bab768` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bab76c"></a> `00bab76c` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bab770"></a> `00bab770` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bab774"></a> `00bab774` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bab778"></a> `00bab778` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab77c"></a> `00bab77c` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab780"></a> `00bab780` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab784"></a> `00bab784` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bab788"></a> `00bab788` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bab78c"></a> `00bab78c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bab790"></a> `00bab790` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bab794"></a> `00bab794` | `f6 ff ff 17` | b 0x00bab76c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bab4fc`](#insn-00bab4fc) 範囲 `[['00bab4fc', '00bab547']]`
  - `CONDITIONAL_JUMP` [`00bab544`](#insn-00bab544) → [`00bab564`](#insn-00bab564)
  - `FALL_THROUGH` [`00bab544`](#insn-00bab544) → [`00bab548`](#insn-00bab548)
- ブロック [`00bab548`](#insn-00bab548) 範囲 `[['00bab548', '00bab54b']]`
  - `FALL_THROUGH` [`00bab548`](#insn-00bab548) → [`00bab54c`](#insn-00bab54c)
- ブロック [`00bab54c`](#insn-00bab54c) 範囲 `[['00bab54c', '00bab553']]`
  - `CONDITIONAL_JUMP` [`00bab550`](#insn-00bab550) → [`00bab564`](#insn-00bab564)
  - `FALL_THROUGH` [`00bab550`](#insn-00bab550) → [`00bab554`](#insn-00bab554)
- ブロック [`00bab554`](#insn-00bab554) 範囲 `[['00bab554', '00bab55f']]`
  - `CONDITIONAL_JUMP` [`00bab55c`](#insn-00bab55c) → [`00bab54c`](#insn-00bab54c)
  - `FALL_THROUGH` [`00bab55c`](#insn-00bab55c) → [`00bab560`](#insn-00bab560)
- ブロック [`00bab560`](#insn-00bab560) 範囲 `[['00bab560', '00bab563']]`
  - `FALL_THROUGH` [`00bab560`](#insn-00bab560) → [`00bab564`](#insn-00bab564)
- ブロック [`00bab564`](#insn-00bab564) 範囲 `[['00bab564', '00bab577']]`
  - `CONDITIONAL_JUMP` [`00bab574`](#insn-00bab574) → [`00bab58c`](#insn-00bab58c)
  - `FALL_THROUGH` [`00bab574`](#insn-00bab574) → [`00bab578`](#insn-00bab578)
- ブロック [`00bab578`](#insn-00bab578) 範囲 `[['00bab578', '00bab57b']]`
  - `UNCONDITIONAL_JUMP` [`00bab578`](#insn-00bab578) → [`00bab764`](#insn-00bab764)
- ブロック [`00bab57c`](#insn-00bab57c) 範囲 `[['00bab57c', '00bab57f']]`
  - `FALL_THROUGH` [`00bab57c`](#insn-00bab57c) → [`00bab580`](#insn-00bab580)
- ブロック [`00bab580`](#insn-00bab580) 範囲 `[['00bab580', '00bab58b']]`
  - `CONDITIONAL_JUMP` [`00bab588`](#insn-00bab588) → [`00bab764`](#insn-00bab764)
  - `FALL_THROUGH` [`00bab588`](#insn-00bab588) → [`00bab58c`](#insn-00bab58c)
- ブロック [`00bab58c`](#insn-00bab58c) 範囲 `[['00bab58c', '00bab593']]`
  - `CONDITIONAL_JUMP` [`00bab590`](#insn-00bab590) → [`00bab764`](#insn-00bab764)
  - `FALL_THROUGH` [`00bab590`](#insn-00bab590) → [`00bab594`](#insn-00bab594)
- ブロック [`00bab594`](#insn-00bab594) 範囲 `[['00bab594', '00bab5db']]`
  - `CONDITIONAL_JUMP` [`00bab5d8`](#insn-00bab5d8) → [`00bab5e4`](#insn-00bab5e4)
  - `FALL_THROUGH` [`00bab5d8`](#insn-00bab5d8) → [`00bab5dc`](#insn-00bab5dc)
- ブロック [`00bab5dc`](#insn-00bab5dc) 範囲 `[['00bab5dc', '00bab5e3']]`
  - `FALL_THROUGH` [`00bab5e0`](#insn-00bab5e0) → [`00bab5e4`](#insn-00bab5e4)
- ブロック [`00bab5e4`](#insn-00bab5e4) 範囲 `[['00bab5e4', '00bab5e7']]`
  - `CONDITIONAL_JUMP` [`00bab5e4`](#insn-00bab5e4) → [`00bab6d0`](#insn-00bab6d0)
  - `FALL_THROUGH` [`00bab5e4`](#insn-00bab5e4) → [`00bab5e8`](#insn-00bab5e8)
- ブロック [`00bab5e8`](#insn-00bab5e8) 範囲 `[['00bab5e8', '00bab5ef']]`
  - `CONDITIONAL_JUMP` [`00bab5ec`](#insn-00bab5ec) → [`00bab6d8`](#insn-00bab6d8)
  - `FALL_THROUGH` [`00bab5ec`](#insn-00bab5ec) → [`00bab5f0`](#insn-00bab5f0)
- ブロック [`00bab5f0`](#insn-00bab5f0) 範囲 `[['00bab5f0', '00bab603']]`
  - `CONDITIONAL_JUMP` [`00bab600`](#insn-00bab600) → [`00bab75c`](#insn-00bab75c)
  - `FALL_THROUGH` [`00bab600`](#insn-00bab600) → [`00bab604`](#insn-00bab604)
- ブロック [`00bab604`](#insn-00bab604) 範囲 `[['00bab604', '00bab60b']]`
  - `CONDITIONAL_JUMP` [`00bab608`](#insn-00bab608) → [`00bab6b8`](#insn-00bab6b8)
  - `FALL_THROUGH` [`00bab608`](#insn-00bab608) → [`00bab60c`](#insn-00bab60c)
- ブロック [`00bab60c`](#insn-00bab60c) 範囲 `[['00bab60c', '00bab637']]`
  - `CONDITIONAL_JUMP` [`00bab634`](#insn-00bab634) → [`00bab640`](#insn-00bab640)
  - `FALL_THROUGH` [`00bab634`](#insn-00bab634) → [`00bab638`](#insn-00bab638)
- ブロック [`00bab638`](#insn-00bab638) 範囲 `[['00bab638', '00bab63f']]`
  - `FALL_THROUGH` [`00bab63c`](#insn-00bab63c) → [`00bab640`](#insn-00bab640)
- ブロック [`00bab640`](#insn-00bab640) 範囲 `[['00bab640', '00bab647']]`
  - `CONDITIONAL_JUMP` [`00bab644`](#insn-00bab644) → [`00bab790`](#insn-00bab790)
  - `FALL_THROUGH` [`00bab644`](#insn-00bab644) → [`00bab648`](#insn-00bab648)
- ブロック [`00bab648`](#insn-00bab648) 範囲 `[['00bab648', '00bab657']]`
  - `CONDITIONAL_JUMP` [`00bab654`](#insn-00bab654) → [`00bab6d0`](#insn-00bab6d0)
  - `FALL_THROUGH` [`00bab654`](#insn-00bab654) → [`00bab658`](#insn-00bab658)
- ブロック [`00bab658`](#insn-00bab658) 範囲 `[['00bab658', '00bab65b']]`
  - `CONDITIONAL_JUMP` [`00bab658`](#insn-00bab658) → [`00bab67c`](#insn-00bab67c)
  - `FALL_THROUGH` [`00bab658`](#insn-00bab658) → [`00bab65c`](#insn-00bab65c)
- ブロック [`00bab65c`](#insn-00bab65c) 範囲 `[['00bab65c', '00bab65f']]`
  - `FALL_THROUGH` [`00bab65c`](#insn-00bab65c) → [`00bab660`](#insn-00bab660)
- ブロック [`00bab660`](#insn-00bab660) 範囲 `[['00bab660', '00bab67b']]`
  - `CONDITIONAL_JUMP` [`00bab678`](#insn-00bab678) → [`00bab660`](#insn-00bab660)
  - `FALL_THROUGH` [`00bab678`](#insn-00bab678) → [`00bab67c`](#insn-00bab67c)
- ブロック [`00bab67c`](#insn-00bab67c) 範囲 `[['00bab67c', '00bab69b']]`
  - `CONDITIONAL_JUMP` [`00bab698`](#insn-00bab698) → [`00bab580`](#insn-00bab580)
  - `FALL_THROUGH` [`00bab698`](#insn-00bab698) → [`00bab69c`](#insn-00bab69c)
- ブロック [`00bab69c`](#insn-00bab69c) 範囲 `[['00bab69c', '00bab6a3']]`
  - `CONDITIONAL_JUMP` [`00bab6a0`](#insn-00bab6a0) → [`00bab57c`](#insn-00bab57c)
  - `FALL_THROUGH` [`00bab6a0`](#insn-00bab6a0) → [`00bab6a4`](#insn-00bab6a4)
- ブロック [`00bab6a4`](#insn-00bab6a4) 範囲 `[['00bab6a4', '00bab6af']]`
  - `CONDITIONAL_JUMP` [`00bab6ac`](#insn-00bab6ac) → [`00bab69c`](#insn-00bab69c)
  - `FALL_THROUGH` [`00bab6ac`](#insn-00bab6ac) → [`00bab6b0`](#insn-00bab6b0)
- ブロック [`00bab6b0`](#insn-00bab6b0) 範囲 `[['00bab6b0', '00bab6b7']]`
  - `UNCONDITIONAL_JUMP` [`00bab6b4`](#insn-00bab6b4) → [`00bab580`](#insn-00bab580)
- ブロック [`00bab6b8`](#insn-00bab6b8) 範囲 `[['00bab6b8', '00bab6cb']]`
  - `CONDITIONAL_JUMP` [`00bab6c8`](#insn-00bab6c8) → [`00bab58c`](#insn-00bab58c)
  - `FALL_THROUGH` [`00bab6c8`](#insn-00bab6c8) → [`00bab6cc`](#insn-00bab6cc)
- ブロック [`00bab6cc`](#insn-00bab6cc) 範囲 `[['00bab6cc', '00bab6cf']]`
  - `UNCONDITIONAL_JUMP` [`00bab6cc`](#insn-00bab6cc) → [`00bab764`](#insn-00bab764)
- ブロック [`00bab6d0`](#insn-00bab6d0) 範囲 `[['00bab6d0', '00bab6d7']]`
  - `UNCONDITIONAL_JUMP` [`00bab6d4`](#insn-00bab6d4) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab6d8`](#insn-00bab6d8) 範囲 `[['00bab6d8', '00bab6eb']]`
  - `CONDITIONAL_JUMP` [`00bab6e8`](#insn-00bab6e8) → [`00bab74c`](#insn-00bab74c)
  - `FALL_THROUGH` [`00bab6e8`](#insn-00bab6e8) → [`00bab6ec`](#insn-00bab6ec)
- ブロック [`00bab6ec`](#insn-00bab6ec) 範囲 `[['00bab6ec', '00bab71b']]`
  - `CONDITIONAL_JUMP` [`00bab718`](#insn-00bab718) → [`00bab724`](#insn-00bab724)
  - `FALL_THROUGH` [`00bab718`](#insn-00bab718) → [`00bab71c`](#insn-00bab71c)
- ブロック [`00bab71c`](#insn-00bab71c) 範囲 `[['00bab71c', '00bab723']]`
  - `FALL_THROUGH` [`00bab720`](#insn-00bab720) → [`00bab724`](#insn-00bab724)
- ブロック [`00bab724`](#insn-00bab724) 範囲 `[['00bab724', '00bab72b']]`
  - `CONDITIONAL_JUMP` [`00bab728`](#insn-00bab728) → [`00bab74c`](#insn-00bab74c)
  - `FALL_THROUGH` [`00bab728`](#insn-00bab728) → [`00bab72c`](#insn-00bab72c)
- ブロック [`00bab72c`](#insn-00bab72c) 範囲 `[['00bab72c', '00bab743']]`
  - `FALL_THROUGH` [`00bab740`](#insn-00bab740) → [`00bab744`](#insn-00bab744)
- ブロック [`00bab744`](#insn-00bab744) 範囲 `[['00bab744', '00bab74b']]`
  - `CONDITIONAL_JUMP` [`00bab748`](#insn-00bab748) → [`00bab6ec`](#insn-00bab6ec)
  - `FALL_THROUGH` [`00bab748`](#insn-00bab748) → [`00bab74c`](#insn-00bab74c)
- ブロック [`00bab74c`](#insn-00bab74c) 範囲 `[['00bab74c', '00bab75b']]`
  - `UNCONDITIONAL_JUMP` [`00bab758`](#insn-00bab758) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab75c`](#insn-00bab75c) 範囲 `[['00bab75c', '00bab763']]`
  - `FALL_THROUGH` [`00bab760`](#insn-00bab760) → [`00bab764`](#insn-00bab764)
- ブロック [`00bab764`](#insn-00bab764) 範囲 `[['00bab764', '00bab76b']]`
  - `FALL_THROUGH` [`00bab768`](#insn-00bab768) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab76c`](#insn-00bab76c) 範囲 `[['00bab76c', '00bab78f']]`
- ブロック [`00bab790`](#insn-00bab790) 範囲 `[['00bab790', '00bab797']]`
  - `UNCONDITIONAL_JUMP` [`00bab794`](#insn-00bab794) → [`00bab76c`](#insn-00bab76c)

## 命令位置別の参照

- [`00bab504`](#insn-00bab504) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab508`](#insn-00bab508) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab50c`](#insn-00bab50c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab510`](#insn-00bab510) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab514`](#insn-00bab514) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab518`](#insn-00bab518) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab540`](#insn-00bab540) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab544`](#insn-00bab544) → [`00bab564`](#insn-00bab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab550`](#insn-00bab550) → [`00bab564`](#insn-00bab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab55c`](#insn-00bab55c) → [`00bab54c`](#insn-00bab54c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab564`](#insn-00bab564) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab574`](#insn-00bab574) → [`00bab58c`](#insn-00bab58c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab578`](#insn-00bab578) → [`00bab764`](#insn-00bab764) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab588`](#insn-00bab588) → [`00bab764`](#insn-00bab764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab590`](#insn-00bab590) → [`00bab764`](#insn-00bab764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5a4`](#insn-00bab5a4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5a8`](#insn-00bab5a8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5b0`](#insn-00bab5b0) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab5b8`](#insn-00bab5b8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5bc`](#insn-00bab5bc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5d0`](#insn-00bab5d0) → [`00be1af0`](../00be1/00be1af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1af0` · 推定シンボル `None` · 推定型 `None`
- [`00bab5d8`](#insn-00bab5d8) → [`00bab5e4`](#insn-00bab5e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5e0`](#insn-00bab5e0) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab5e4`](#insn-00bab5e4) → [`00bab6d0`](#insn-00bab6d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5ec`](#insn-00bab5ec) → [`00bab6d8`](#insn-00bab6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab600`](#insn-00bab600) → [`00bab75c`](#insn-00bab75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab608`](#insn-00bab608) → [`00bab6b8`](#insn-00bab6b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab60c`](#insn-00bab60c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab614`](#insn-00bab614) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab61c`](#insn-00bab61c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab62c`](#insn-00bab62c) → [`00be1b00`](../00be1/00be1b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b00` · 推定シンボル `None` · 推定型 `None`
- [`00bab634`](#insn-00bab634) → [`00bab640`](#insn-00bab640) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab63c`](#insn-00bab63c) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab644`](#insn-00bab644) → [`00bab790`](#insn-00bab790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab654`](#insn-00bab654) → [`00bab6d0`](#insn-00bab6d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab658`](#insn-00bab658) → [`00bab67c`](#insn-00bab67c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab678`](#insn-00bab678) → [`00bab660`](#insn-00bab660) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab67c`](#insn-00bab67c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab698`](#insn-00bab698) → [`00bab580`](#insn-00bab580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6a0`](#insn-00bab6a0) → [`00bab57c`](#insn-00bab57c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6ac`](#insn-00bab6ac) → [`00bab69c`](#insn-00bab69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6b4`](#insn-00bab6b4) → [`00bab580`](#insn-00bab580) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6b8`](#insn-00bab6b8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6c8`](#insn-00bab6c8) → [`00bab58c`](#insn-00bab58c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6cc`](#insn-00bab6cc) → [`00bab764`](#insn-00bab764) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d4`](#insn-00bab6d4) → [`00bab76c`](#insn-00bab76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d8`](#insn-00bab6d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6e8`](#insn-00bab6e8) → [`00bab74c`](#insn-00bab74c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6ec`](#insn-00bab6ec) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6f8`](#insn-00bab6f8) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab700`](#insn-00bab700) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab710`](#insn-00bab710) → [`00be1b00`](../00be1/00be1b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b00` · 推定シンボル `None` · 推定型 `None`
- [`00bab718`](#insn-00bab718) → [`00bab724`](#insn-00bab724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab720`](#insn-00bab720) → [`00be1530`](../00be1/00be1530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1530` · 推定シンボル `None` · 推定型 `None`
- [`00bab728`](#insn-00bab728) → [`00bab74c`](#insn-00bab74c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab738`](#insn-00bab738) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab748`](#insn-00bab748) → [`00bab6ec`](#insn-00bab6ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab74c`](#insn-00bab74c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab758`](#insn-00bab758) → [`00bab76c`](#insn-00bab76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab75c`](#insn-00bab75c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab76c`](#insn-00bab76c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab770`](#insn-00bab770) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab774`](#insn-00bab774) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab778`](#insn-00bab778) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab77c`](#insn-00bab77c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab780`](#insn-00bab780) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab794`](#insn-00bab794) → [`00bab76c`](#insn-00bab76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab504`](#insn-00bab504)

~~~json
{
  "source": "00bab504",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab508`](#insn-00bab508)

~~~json
{
  "source": "00bab508",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab50c`](#insn-00bab50c)

~~~json
{
  "source": "00bab50c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab510`](#insn-00bab510)

~~~json
{
  "source": "00bab510",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab514`](#insn-00bab514)

~~~json
{
  "source": "00bab514",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab518`](#insn-00bab518)

~~~json
{
  "source": "00bab518",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab540`](#insn-00bab540)

~~~json
{
  "source": "00bab540",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab544`](#insn-00bab544)

~~~json
{
  "source": "00bab544",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab550`](#insn-00bab550)

~~~json
{
  "source": "00bab550",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab55c`](#insn-00bab55c)

~~~json
{
  "source": "00bab55c",
  "target": "00bab54c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab564`](#insn-00bab564)

~~~json
{
  "source": "00bab564",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab574`](#insn-00bab574)

~~~json
{
  "source": "00bab574",
  "target": "00bab58c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab578`](#insn-00bab578)

~~~json
{
  "source": "00bab578",
  "target": "00bab764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab588`](#insn-00bab588)

~~~json
{
  "source": "00bab588",
  "target": "00bab764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab590`](#insn-00bab590)

~~~json
{
  "source": "00bab590",
  "target": "00bab764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5a4`](#insn-00bab5a4)

~~~json
{
  "source": "00bab5a4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5a8`](#insn-00bab5a8)

~~~json
{
  "source": "00bab5a8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5b0`](#insn-00bab5b0)

~~~json
{
  "source": "00bab5b0",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab5b8`](#insn-00bab5b8)

~~~json
{
  "source": "00bab5b8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5bc`](#insn-00bab5bc)

~~~json
{
  "source": "00bab5bc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5d0`](#insn-00bab5d0)

~~~json
{
  "source": "00bab5d0",
  "target": "00be1af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab5d8`](#insn-00bab5d8)

~~~json
{
  "source": "00bab5d8",
  "target": "00bab5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5e0`](#insn-00bab5e0)

~~~json
{
  "source": "00bab5e0",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab5e4`](#insn-00bab5e4)

~~~json
{
  "source": "00bab5e4",
  "target": "00bab6d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5ec`](#insn-00bab5ec)

~~~json
{
  "source": "00bab5ec",
  "target": "00bab6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab600`](#insn-00bab600)

~~~json
{
  "source": "00bab600",
  "target": "00bab75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab608`](#insn-00bab608)

~~~json
{
  "source": "00bab608",
  "target": "00bab6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab60c`](#insn-00bab60c)

~~~json
{
  "source": "00bab60c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab614`](#insn-00bab614)

~~~json
{
  "source": "00bab614",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab61c`](#insn-00bab61c)

~~~json
{
  "source": "00bab61c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab62c`](#insn-00bab62c)

~~~json
{
  "source": "00bab62c",
  "target": "00be1b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab634`](#insn-00bab634)

~~~json
{
  "source": "00bab634",
  "target": "00bab640",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab63c`](#insn-00bab63c)

~~~json
{
  "source": "00bab63c",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab644`](#insn-00bab644)

~~~json
{
  "source": "00bab644",
  "target": "00bab790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab654`](#insn-00bab654)

~~~json
{
  "source": "00bab654",
  "target": "00bab6d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab658`](#insn-00bab658)

~~~json
{
  "source": "00bab658",
  "target": "00bab67c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab678`](#insn-00bab678)

~~~json
{
  "source": "00bab678",
  "target": "00bab660",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab67c`](#insn-00bab67c)

~~~json
{
  "source": "00bab67c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab698`](#insn-00bab698)

~~~json
{
  "source": "00bab698",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6a0`](#insn-00bab6a0)

~~~json
{
  "source": "00bab6a0",
  "target": "00bab57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6ac`](#insn-00bab6ac)

~~~json
{
  "source": "00bab6ac",
  "target": "00bab69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6b4`](#insn-00bab6b4)

~~~json
{
  "source": "00bab6b4",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6b8`](#insn-00bab6b8)

~~~json
{
  "source": "00bab6b8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6c8`](#insn-00bab6c8)

~~~json
{
  "source": "00bab6c8",
  "target": "00bab58c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6cc`](#insn-00bab6cc)

~~~json
{
  "source": "00bab6cc",
  "target": "00bab764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d4`](#insn-00bab6d4)

~~~json
{
  "source": "00bab6d4",
  "target": "00bab76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d8`](#insn-00bab6d8)

~~~json
{
  "source": "00bab6d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6e8`](#insn-00bab6e8)

~~~json
{
  "source": "00bab6e8",
  "target": "00bab74c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6ec`](#insn-00bab6ec)

~~~json
{
  "source": "00bab6ec",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6f8`](#insn-00bab6f8)

~~~json
{
  "source": "00bab6f8",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab700`](#insn-00bab700)

~~~json
{
  "source": "00bab700",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab710`](#insn-00bab710)

~~~json
{
  "source": "00bab710",
  "target": "00be1b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab718`](#insn-00bab718)

~~~json
{
  "source": "00bab718",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab720`](#insn-00bab720)

~~~json
{
  "source": "00bab720",
  "target": "00be1530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab728`](#insn-00bab728)

~~~json
{
  "source": "00bab728",
  "target": "00bab74c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab738`](#insn-00bab738)

~~~json
{
  "source": "00bab738",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab748`](#insn-00bab748)

~~~json
{
  "source": "00bab748",
  "target": "00bab6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab74c`](#insn-00bab74c)

~~~json
{
  "source": "00bab74c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab758`](#insn-00bab758)

~~~json
{
  "source": "00bab758",
  "target": "00bab76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab75c`](#insn-00bab75c)

~~~json
{
  "source": "00bab75c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab76c`](#insn-00bab76c)

~~~json
{
  "source": "00bab76c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab770`](#insn-00bab770)

~~~json
{
  "source": "00bab770",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab774`](#insn-00bab774)

~~~json
{
  "source": "00bab774",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab778`](#insn-00bab778)

~~~json
{
  "source": "00bab778",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab77c`](#insn-00bab77c)

~~~json
{
  "source": "00bab77c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab780`](#insn-00bab780)

~~~json
{
  "source": "00bab780",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab794`](#insn-00bab794)

~~~json
{
  "source": "00bab794",
  "target": "00bab76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
