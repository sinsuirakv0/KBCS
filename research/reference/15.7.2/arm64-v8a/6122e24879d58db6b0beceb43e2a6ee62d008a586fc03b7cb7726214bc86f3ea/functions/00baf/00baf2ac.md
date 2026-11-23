# 00baf2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baf374`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-c9d4f414c076ad8b1ed1afa5d15a08f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf2ac",
  "name": "_ZNSt6__ndk115numpunct_bynameIcE6__initEPKc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "86fdfff5ed31b49358e3d310ef60eba5966b7cd42fe0515385987305b4c53512",
  "source_text_sha256": "86fdfff5ed31b49358e3d310ef60eba5966b7cd42fe0515385987305b4c53512",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baf2ac",
        "00baf503"
      ]
    ],
    "bytes_sha256": "a78b76713ddd9074ab4d3213317b8226cc42bd1a05860a22add798a5316ea554",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1b70](../00be1/00be1b70.md)

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [0041e0fc](../0041e/0041e0fc.md)
- [00b7501c](../00b75/00b7501c.md)
- [00ba89b8](../00ba8/00ba89b8.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bde8d0](../00bde/00bde8d0.md)
- [00be0eb0](../00be0/00be0eb0.md)
- [00be1470](../00be1/00be1470.md)
- [00be1480](../00be1/00be1480.md)
- [00be1830](../00be1/00be1830.md)
- [00be1a10](../00be1/00be1a10.md)
- [00be1a70](../00be1/00be1a70.md)
- [00be1b80](../00be1/00be1b80.md)

## 関連文字列（未確認候補）

~~~text
"numpunct_byname<char>::numpunct_byname failed to construct for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3487 bytes

~~~c

void _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc(long param_1,char *param_2)

{
  wchar_t __c;
  int iVar1;
  __locale_t __dataset;
  __locale_t p_Var2;
  lconv *plVar3;
  size_t sVar4;
  char *pcVar5;
  mbstate_t local_80 [3];
  undefined8 local_68;
  long local_58;
  __locale_t local_50;
  wchar_t local_44;
  
  iVar1 = strcmp(param_2,"C");
  if (iVar1 != 0) {
    __dataset = newlocale(0x1fbf,param_2,(__locale_t)0x0);
    local_50 = __dataset;
    if (__dataset == (__locale_t)0x0) {
      FUN_0041b298(local_80,param_2);
                    /* try { // try from 00baf4e0 to 00caf583 has its CatchHandler @ 00baf60c */
      FUN_00ba89b8(&local_68,"numpunct_byname<char>::numpunct_byname failed to construct for ",
                   local_80);
      if (((byte)local_68 & 1) == 0) {
        local_58 = (long)&local_68 + 1;
      }
      _ZNSt6__ndk121__throw_runtime_errorEPKc(local_58);
                    /* WARNING: Subroutine does not return */
      FUN_0041e0fc();
    }
    p_Var2 = uselocale(__dataset);
    local_68 = p_Var2;
    plVar3 = localeconv();
    if (p_Var2 != (__locale_t)0x0) {
      uselocale(p_Var2);
    }
    pcVar5 = plVar3->decimal_point;
    if (*pcVar5 != '\0') {
      if (pcVar5[1] == '\0') {
        *(char *)(param_1 + 0x10) = *pcVar5;
      }
      else {
        local_80[0].__count = 0;
        local_80[0].__value = (_union_27)0x0;
        sVar4 = strlen(pcVar5);
        p_Var2 = uselocale(__dataset);
        local_68 = p_Var2;
        sVar4 = mbrtowc(&local_44,pcVar5,sVar4,local_80);
        if (p_Var2 != (__locale_t)0x0) {
          uselocale(p_Var2);
        }
        __c = local_44;
                    /* catch() { ... } // from try @ 00baf20c with catch @ 00baf378 */
        if (sVar4 < 0xfffffffffffffffe) {
          p_Var2 = uselocale(__dataset);
          local_68 = p_Var2;
          iVar1 = wctob(__c);
          if (p_Var2 != (__locale_t)0x0) {
            uselocale(p_Var2);
          }
          if (((iVar1 != -1) || (iVar1 = 0x20, __c == L'\x202f')) || (__c == L'\xa0')) {
            *(char *)(param_1 + 0x10) = (char)iVar1;
          }
        }
      }
    }
    pcVar5 = plVar3->thousands_sep;
    if (*pcVar5 != '\0') {
      if (pcVar5[1] == '\0') {
        *(char *)(param_1 + 0x11) = *pcVar5;
      }
      else {
        local_80[0].__count = 0;
        local_80[0].__value = (_union_27)0x0;
        sVar4 = strlen(pcVar5);
        p_Var2 = uselocale(__dataset);
        local_68 = p_Var2;
        sVar4 = mbrtowc(&local_44,pcVar5,sVar4,local_80);
        if (p_Var2 != (__locale_t)0x0) {
          uselocale(p_Var2);
        }
        if (sVar4 < 0xfffffffffffffffe) {
          p_Var2 = uselocale(__dataset);
          local_68 = p_Var2;
          iVar1 = wctob(local_44);
          if (p_Var2 != (__locale_t)0x0) {
                    /* catch() { ... } // from try @ 00baf584 with catch @ 00baf448
                       catch() { ... } // from try @ 00baf600 with catch @ 00baf448 */
            uselocale(p_Var2);
          }
                    /* try { // try from 00baf4bc to 00caf4d7 has its CatchHandler @ 00baf608 */
          if (((iVar1 != -1) || (iVar1 = 0x20, local_44 == L'\x202f')) || (local_44 == L'\xa0')) {
            *(char *)(param_1 + 0x11) = (char)iVar1;
          }
        }
      }
    }
    FUN_00b7501c(param_1 + 0x18,plVar3->grouping);
    freelocale(__dataset);
  }
                    /* try { // try from 00baf480 to 00caf49b has its CatchHandler @ 00baf600 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baf2ac"></a> `00baf2ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baf2b0"></a> `00baf2b0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00baf2b4"></a> `00baf2b4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf2b8"></a> `00baf2b8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf2bc"></a> `00baf2bc` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00baf2c0"></a> `00baf2c0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baf2c4"></a> `00baf2c4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baf2c8"></a> `00baf2c8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00baf2cc"></a> `00baf2cc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baf2d0"></a> `00baf2d0` | `a1 b7 ff d0` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00baf2d4"></a> `00baf2d4` | `21 28 1a 91` | add x1,x1,#0x68a | `FALL_THROUGH`
<a id="insn-00baf2d8"></a> `00baf2d8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baf2dc"></a> `00baf2dc` | `7d bd 00 94` | bl 0x00bde8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf2e0"></a> `00baf2e0` | `a0 0c 00 34` | cbz w0,0x00baf474 | `CONDITIONAL_JUMP`
<a id="insn-00baf2e4"></a> `00baf2e4` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00baf2e8"></a> `00baf2e8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baf2ec"></a> `00baf2ec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00baf2f0"></a> `00baf2f0` | `60 c8 00 94` | bl 0x00be1470 | `UNCONDITIONAL_CALL`
<a id="insn-00baf2f4"></a> `00baf2f4` | `a0 03 1f f8` | stur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00baf2f8"></a> `00baf2f8` | `80 0e 00 b4` | cbz x0,0x00baf4c8 | `CONDITIONAL_JUMP`
<a id="insn-00baf2fc"></a> `00baf2fc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baf300"></a> `00baf300` | `60 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf304"></a> `00baf304` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baf308"></a> `00baf308` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf30c"></a> `00baf30c` | `1d ca 00 94` | bl 0x00be1b80 | `UNCONDITIONAL_CALL`
<a id="insn-00baf310"></a> `00baf310` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00baf314"></a> `00baf314` | `76 00 00 b4` | cbz x22,0x00baf320 | `CONDITIONAL_JUMP`
<a id="insn-00baf318"></a> `00baf318` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baf31c"></a> `00baf31c` | `59 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf320"></a> `00baf320` | `b6 02 40 f9` | ldr x22,[x21] | `FALL_THROUGH`
<a id="insn-00baf324"></a> `00baf324` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00baf328"></a> `00baf328` | `c8 04 00 34` | cbz w8,0x00baf3c0 | `CONDITIONAL_JUMP`
<a id="insn-00baf32c"></a> `00baf32c` | `c9 06 40 39` | ldrb w9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00baf330"></a> `00baf330` | `69 04 00 34` | cbz w9,0x00baf3bc | `CONDITIONAL_JUMP`
<a id="insn-00baf334"></a> `00baf334` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baf338"></a> `00baf338` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00baf33c"></a> `00baf33c` | `55 af 00 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00baf340"></a> `00baf340` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00baf344"></a> `00baf344` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf348"></a> `00baf348` | `4e c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf34c"></a> `00baf34c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00baf350"></a> `00baf350` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf354"></a> `00baf354` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00baf358"></a> `00baf358` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00baf35c"></a> `00baf35c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00baf360"></a> `00baf360` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00baf364"></a> `00baf364` | `c3 c9 00 94` | bl 0x00be1a70 | `UNCONDITIONAL_CALL`
<a id="insn-00baf368"></a> `00baf368` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baf36c"></a> `00baf36c` | `77 00 00 b4` | cbz x23,0x00baf378 | `CONDITIONAL_JUMP`
<a id="insn-00baf370"></a> `00baf370` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00baf374"></a> `00baf374` | `43 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf378"></a> `00baf378` | `df 0a 00 b1` | cmn x22,#0x2 | `FALL_THROUGH`
<a id="insn-00baf37c"></a> `00baf37c` | `22 02 00 54` | b.cs 0x00baf3c0 | `CONDITIONAL_JUMP`
<a id="insn-00baf380"></a> `00baf380` | `b6 c3 5f b8` | ldur w22,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00baf384"></a> `00baf384` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf388"></a> `00baf388` | `3e c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf38c"></a> `00baf38c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00baf390"></a> `00baf390` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf394"></a> `00baf394` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00baf398"></a> `00baf398` | `9e c9 00 94` | bl 0x00be1a10 | `UNCONDITIONAL_CALL`
<a id="insn-00baf39c"></a> `00baf39c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00baf3a0"></a> `00baf3a0` | `78 00 00 b4` | cbz x24,0x00baf3ac | `CONDITIONAL_JUMP`
<a id="insn-00baf3a4"></a> `00baf3a4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00baf3a8"></a> `00baf3a8` | `36 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf3ac"></a> `00baf3ac` | `ff 06 00 31` | cmn w23,#0x1 | `FALL_THROUGH`
<a id="insn-00baf3b0"></a> `00baf3b0` | `00 07 00 54` | b.eq 0x00baf490 | `CONDITIONAL_JUMP`
<a id="insn-00baf3b4"></a> `00baf3b4` | `77 42 00 39` | strb w23,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00baf3b8"></a> `00baf3b8` | `02 00 00 14` | b 0x00baf3c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf3bc"></a> `00baf3bc` | `68 42 00 39` | strb w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00baf3c0"></a> `00baf3c0` | `b6 06 40 f9` | ldr x22,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00baf3c4"></a> `00baf3c4` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00baf3c8"></a> `00baf3c8` | `c8 04 00 34` | cbz w8,0x00baf460 | `CONDITIONAL_JUMP`
<a id="insn-00baf3cc"></a> `00baf3cc` | `c9 06 40 39` | ldrb w9,[x22, #0x1] | `FALL_THROUGH`
<a id="insn-00baf3d0"></a> `00baf3d0` | `69 04 00 34` | cbz w9,0x00baf45c | `CONDITIONAL_JUMP`
<a id="insn-00baf3d4"></a> `00baf3d4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baf3d8"></a> `00baf3d8` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00baf3dc"></a> `00baf3dc` | `2d af 00 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00baf3e0"></a> `00baf3e0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00baf3e4"></a> `00baf3e4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf3e8"></a> `00baf3e8` | `26 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf3ec"></a> `00baf3ec` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00baf3f0"></a> `00baf3f0` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf3f4"></a> `00baf3f4` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00baf3f8"></a> `00baf3f8` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00baf3fc"></a> `00baf3fc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00baf400"></a> `00baf400` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00baf404"></a> `00baf404` | `9b c9 00 94` | bl 0x00be1a70 | `UNCONDITIONAL_CALL`
<a id="insn-00baf408"></a> `00baf408` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baf40c"></a> `00baf40c` | `77 00 00 b4` | cbz x23,0x00baf418 | `CONDITIONAL_JUMP`
<a id="insn-00baf410"></a> `00baf410` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00baf414"></a> `00baf414` | `1b c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf418"></a> `00baf418` | `df 0a 00 b1` | cmn x22,#0x2 | `FALL_THROUGH`
<a id="insn-00baf41c"></a> `00baf41c` | `22 02 00 54` | b.cs 0x00baf460 | `CONDITIONAL_JUMP`
<a id="insn-00baf420"></a> `00baf420` | `b6 c3 5f b8` | ldur w22,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00baf424"></a> `00baf424` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf428"></a> `00baf428` | `16 c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf42c"></a> `00baf42c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00baf430"></a> `00baf430` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf434"></a> `00baf434` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00baf438"></a> `00baf438` | `76 c9 00 94` | bl 0x00be1a10 | `UNCONDITIONAL_CALL`
<a id="insn-00baf43c"></a> `00baf43c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00baf440"></a> `00baf440` | `78 00 00 b4` | cbz x24,0x00baf44c | `CONDITIONAL_JUMP`
<a id="insn-00baf444"></a> `00baf444` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00baf448"></a> `00baf448` | `0e c8 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baf44c"></a> `00baf44c` | `ff 06 00 31` | cmn w23,#0x1 | `FALL_THROUGH`
<a id="insn-00baf450"></a> `00baf450` | `e0 02 00 54` | b.eq 0x00baf4ac | `CONDITIONAL_JUMP`
<a id="insn-00baf454"></a> `00baf454` | `77 46 00 39` | strb w23,[x19, #0x11] | `FALL_THROUGH`
<a id="insn-00baf458"></a> `00baf458` | `02 00 00 14` | b 0x00baf460 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf45c"></a> `00baf45c` | `68 46 00 39` | strb w8,[x19, #0x11] | `FALL_THROUGH`
<a id="insn-00baf460"></a> `00baf460` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00baf464"></a> `00baf464` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00baf468"></a> `00baf468` | `ed 16 ff 97` | bl 0x00b7501c | `UNCONDITIONAL_CALL`
<a id="insn-00baf46c"></a> `00baf46c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf470"></a> `00baf470` | `f0 c8 00 94` | bl 0x00be1830 | `UNCONDITIONAL_CALL`
<a id="insn-00baf474"></a> `00baf474` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baf478"></a> `00baf478` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00baf47c"></a> `00baf47c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baf480"></a> `00baf480` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf484"></a> `00baf484` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00baf488"></a> `00baf488` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baf48c"></a> `00baf48c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baf490"></a> `00baf490` | `e8 05 84 52` | mov w8,#0x202f | `FALL_THROUGH`
<a id="insn-00baf494"></a> `00baf494` | `17 04 80 52` | mov w23,#0x20 | `FALL_THROUGH`
<a id="insn-00baf498"></a> `00baf498` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00baf49c"></a> `00baf49c` | `c0 f8 ff 54` | b.eq 0x00baf3b4 | `CONDITIONAL_JUMP`
<a id="insn-00baf4a0"></a> `00baf4a0` | `df 82 02 71` | cmp w22,#0xa0 | `FALL_THROUGH`
<a id="insn-00baf4a4"></a> `00baf4a4` | `80 f8 ff 54` | b.eq 0x00baf3b4 | `CONDITIONAL_JUMP`
<a id="insn-00baf4a8"></a> `00baf4a8` | `c6 ff ff 17` | b 0x00baf3c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf4ac"></a> `00baf4ac` | `e8 05 84 52` | mov w8,#0x202f | `FALL_THROUGH`
<a id="insn-00baf4b0"></a> `00baf4b0` | `17 04 80 52` | mov w23,#0x20 | `FALL_THROUGH`
<a id="insn-00baf4b4"></a> `00baf4b4` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00baf4b8"></a> `00baf4b8` | `e0 fc ff 54` | b.eq 0x00baf454 | `CONDITIONAL_JUMP`
<a id="insn-00baf4bc"></a> `00baf4bc` | `df 82 02 71` | cmp w22,#0xa0 | `FALL_THROUGH`
<a id="insn-00baf4c0"></a> `00baf4c0` | `a0 fc ff 54` | b.eq 0x00baf454 | `CONDITIONAL_JUMP`
<a id="insn-00baf4c4"></a> `00baf4c4` | `e7 ff ff 17` | b 0x00baf460 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf4c8"></a> `00baf4c8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00baf4cc"></a> `00baf4cc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baf4d0"></a> `00baf4d0` | `72 af e1 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00baf4d4"></a> `00baf4d4` | `40 b7 ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00baf4d8"></a> `00baf4d8` | `00 68 26 91` | add x0,x0,#0x99a | `FALL_THROUGH`
<a id="insn-00baf4dc"></a> `00baf4dc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00baf4e0"></a> `00baf4e0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baf4e4"></a> `00baf4e4` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00baf4e8"></a> `00baf4e8` | `34 e5 ff 97` | bl 0x00ba89b8 | `UNCONDITIONAL_CALL`
<a id="insn-00baf4ec"></a> `00baf4ec` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00baf4f0"></a> `00baf4f0` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00baf4f4"></a> `00baf4f4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baf4f8"></a> `00baf4f8` | `20 15 93 9a` | csinc x0,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00baf4fc"></a> `00baf4fc` | `6d c6 00 94` | bl 0x00be0eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf500"></a> `00baf500` | `ff ba e1 97` | bl 0x0041e0fc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baf2ac`](#insn-00baf2ac) 範囲 `[['00baf2ac', '00baf2e3']]`
  - `CONDITIONAL_JUMP` [`00baf2e0`](#insn-00baf2e0) → [`00baf474`](#insn-00baf474)
  - `FALL_THROUGH` [`00baf2e0`](#insn-00baf2e0) → [`00baf2e4`](#insn-00baf2e4)
- ブロック [`00baf2e4`](#insn-00baf2e4) 範囲 `[['00baf2e4', '00baf2fb']]`
  - `CONDITIONAL_JUMP` [`00baf2f8`](#insn-00baf2f8) → [`00baf4c8`](#insn-00baf4c8)
  - `FALL_THROUGH` [`00baf2f8`](#insn-00baf2f8) → [`00baf2fc`](#insn-00baf2fc)
- ブロック [`00baf2fc`](#insn-00baf2fc) 範囲 `[['00baf2fc', '00baf317']]`
  - `CONDITIONAL_JUMP` [`00baf314`](#insn-00baf314) → [`00baf320`](#insn-00baf320)
  - `FALL_THROUGH` [`00baf314`](#insn-00baf314) → [`00baf318`](#insn-00baf318)
- ブロック [`00baf318`](#insn-00baf318) 範囲 `[['00baf318', '00baf31f']]`
  - `FALL_THROUGH` [`00baf31c`](#insn-00baf31c) → [`00baf320`](#insn-00baf320)
- ブロック [`00baf320`](#insn-00baf320) 範囲 `[['00baf320', '00baf32b']]`
  - `CONDITIONAL_JUMP` [`00baf328`](#insn-00baf328) → [`00baf3c0`](#insn-00baf3c0)
  - `FALL_THROUGH` [`00baf328`](#insn-00baf328) → [`00baf32c`](#insn-00baf32c)
- ブロック [`00baf32c`](#insn-00baf32c) 範囲 `[['00baf32c', '00baf333']]`
  - `CONDITIONAL_JUMP` [`00baf330`](#insn-00baf330) → [`00baf3bc`](#insn-00baf3bc)
  - `FALL_THROUGH` [`00baf330`](#insn-00baf330) → [`00baf334`](#insn-00baf334)
- ブロック [`00baf334`](#insn-00baf334) 範囲 `[['00baf334', '00baf36f']]`
  - `CONDITIONAL_JUMP` [`00baf36c`](#insn-00baf36c) → [`00baf378`](#insn-00baf378)
  - `FALL_THROUGH` [`00baf36c`](#insn-00baf36c) → [`00baf370`](#insn-00baf370)
- ブロック [`00baf370`](#insn-00baf370) 範囲 `[['00baf370', '00baf377']]`
  - `FALL_THROUGH` [`00baf374`](#insn-00baf374) → [`00baf378`](#insn-00baf378)
- ブロック [`00baf378`](#insn-00baf378) 範囲 `[['00baf378', '00baf37f']]`
  - `CONDITIONAL_JUMP` [`00baf37c`](#insn-00baf37c) → [`00baf3c0`](#insn-00baf3c0)
  - `FALL_THROUGH` [`00baf37c`](#insn-00baf37c) → [`00baf380`](#insn-00baf380)
- ブロック [`00baf380`](#insn-00baf380) 範囲 `[['00baf380', '00baf3a3']]`
  - `CONDITIONAL_JUMP` [`00baf3a0`](#insn-00baf3a0) → [`00baf3ac`](#insn-00baf3ac)
  - `FALL_THROUGH` [`00baf3a0`](#insn-00baf3a0) → [`00baf3a4`](#insn-00baf3a4)
- ブロック [`00baf3a4`](#insn-00baf3a4) 範囲 `[['00baf3a4', '00baf3ab']]`
  - `FALL_THROUGH` [`00baf3a8`](#insn-00baf3a8) → [`00baf3ac`](#insn-00baf3ac)
- ブロック [`00baf3ac`](#insn-00baf3ac) 範囲 `[['00baf3ac', '00baf3b3']]`
  - `CONDITIONAL_JUMP` [`00baf3b0`](#insn-00baf3b0) → [`00baf490`](#insn-00baf490)
  - `FALL_THROUGH` [`00baf3b0`](#insn-00baf3b0) → [`00baf3b4`](#insn-00baf3b4)
- ブロック [`00baf3b4`](#insn-00baf3b4) 範囲 `[['00baf3b4', '00baf3bb']]`
  - `UNCONDITIONAL_JUMP` [`00baf3b8`](#insn-00baf3b8) → [`00baf3c0`](#insn-00baf3c0)
- ブロック [`00baf3bc`](#insn-00baf3bc) 範囲 `[['00baf3bc', '00baf3bf']]`
  - `FALL_THROUGH` [`00baf3bc`](#insn-00baf3bc) → [`00baf3c0`](#insn-00baf3c0)
- ブロック [`00baf3c0`](#insn-00baf3c0) 範囲 `[['00baf3c0', '00baf3cb']]`
  - `CONDITIONAL_JUMP` [`00baf3c8`](#insn-00baf3c8) → [`00baf460`](#insn-00baf460)
  - `FALL_THROUGH` [`00baf3c8`](#insn-00baf3c8) → [`00baf3cc`](#insn-00baf3cc)
- ブロック [`00baf3cc`](#insn-00baf3cc) 範囲 `[['00baf3cc', '00baf3d3']]`
  - `CONDITIONAL_JUMP` [`00baf3d0`](#insn-00baf3d0) → [`00baf45c`](#insn-00baf45c)
  - `FALL_THROUGH` [`00baf3d0`](#insn-00baf3d0) → [`00baf3d4`](#insn-00baf3d4)
- ブロック [`00baf3d4`](#insn-00baf3d4) 範囲 `[['00baf3d4', '00baf40f']]`
  - `CONDITIONAL_JUMP` [`00baf40c`](#insn-00baf40c) → [`00baf418`](#insn-00baf418)
  - `FALL_THROUGH` [`00baf40c`](#insn-00baf40c) → [`00baf410`](#insn-00baf410)
- ブロック [`00baf410`](#insn-00baf410) 範囲 `[['00baf410', '00baf417']]`
  - `FALL_THROUGH` [`00baf414`](#insn-00baf414) → [`00baf418`](#insn-00baf418)
- ブロック [`00baf418`](#insn-00baf418) 範囲 `[['00baf418', '00baf41f']]`
  - `CONDITIONAL_JUMP` [`00baf41c`](#insn-00baf41c) → [`00baf460`](#insn-00baf460)
  - `FALL_THROUGH` [`00baf41c`](#insn-00baf41c) → [`00baf420`](#insn-00baf420)
- ブロック [`00baf420`](#insn-00baf420) 範囲 `[['00baf420', '00baf443']]`
  - `CONDITIONAL_JUMP` [`00baf440`](#insn-00baf440) → [`00baf44c`](#insn-00baf44c)
  - `FALL_THROUGH` [`00baf440`](#insn-00baf440) → [`00baf444`](#insn-00baf444)
- ブロック [`00baf444`](#insn-00baf444) 範囲 `[['00baf444', '00baf447']]`
  - `FALL_THROUGH` [`00baf444`](#insn-00baf444) → [`00baf448`](#insn-00baf448)
- ブロック [`00baf448`](#insn-00baf448) 範囲 `[['00baf448', '00baf44b']]`
  - `FALL_THROUGH` [`00baf448`](#insn-00baf448) → [`00baf44c`](#insn-00baf44c)
- ブロック [`00baf44c`](#insn-00baf44c) 範囲 `[['00baf44c', '00baf453']]`
  - `CONDITIONAL_JUMP` [`00baf450`](#insn-00baf450) → [`00baf4ac`](#insn-00baf4ac)
  - `FALL_THROUGH` [`00baf450`](#insn-00baf450) → [`00baf454`](#insn-00baf454)
- ブロック [`00baf454`](#insn-00baf454) 範囲 `[['00baf454', '00baf45b']]`
  - `UNCONDITIONAL_JUMP` [`00baf458`](#insn-00baf458) → [`00baf460`](#insn-00baf460)
- ブロック [`00baf45c`](#insn-00baf45c) 範囲 `[['00baf45c', '00baf45f']]`
  - `FALL_THROUGH` [`00baf45c`](#insn-00baf45c) → [`00baf460`](#insn-00baf460)
- ブロック [`00baf460`](#insn-00baf460) 範囲 `[['00baf460', '00baf473']]`
  - `FALL_THROUGH` [`00baf470`](#insn-00baf470) → [`00baf474`](#insn-00baf474)
- ブロック [`00baf474`](#insn-00baf474) 範囲 `[['00baf474', '00baf47f']]`
  - `FALL_THROUGH` [`00baf47c`](#insn-00baf47c) → [`00baf480`](#insn-00baf480)
- ブロック [`00baf480`](#insn-00baf480) 範囲 `[['00baf480', '00baf48f']]`
- ブロック [`00baf490`](#insn-00baf490) 範囲 `[['00baf490', '00baf49f']]`
  - `CONDITIONAL_JUMP` [`00baf49c`](#insn-00baf49c) → [`00baf3b4`](#insn-00baf3b4)
  - `FALL_THROUGH` [`00baf49c`](#insn-00baf49c) → [`00baf4a0`](#insn-00baf4a0)
- ブロック [`00baf4a0`](#insn-00baf4a0) 範囲 `[['00baf4a0', '00baf4a7']]`
  - `CONDITIONAL_JUMP` [`00baf4a4`](#insn-00baf4a4) → [`00baf3b4`](#insn-00baf3b4)
  - `FALL_THROUGH` [`00baf4a4`](#insn-00baf4a4) → [`00baf4a8`](#insn-00baf4a8)
- ブロック [`00baf4a8`](#insn-00baf4a8) 範囲 `[['00baf4a8', '00baf4ab']]`
  - `UNCONDITIONAL_JUMP` [`00baf4a8`](#insn-00baf4a8) → [`00baf3c0`](#insn-00baf3c0)
- ブロック [`00baf4ac`](#insn-00baf4ac) 範囲 `[['00baf4ac', '00baf4bb']]`
  - `CONDITIONAL_JUMP` [`00baf4b8`](#insn-00baf4b8) → [`00baf454`](#insn-00baf454)
  - `FALL_THROUGH` [`00baf4b8`](#insn-00baf4b8) → [`00baf4bc`](#insn-00baf4bc)
- ブロック [`00baf4bc`](#insn-00baf4bc) 範囲 `[['00baf4bc', '00baf4c3']]`
  - `CONDITIONAL_JUMP` [`00baf4c0`](#insn-00baf4c0) → [`00baf454`](#insn-00baf454)
  - `FALL_THROUGH` [`00baf4c0`](#insn-00baf4c0) → [`00baf4c4`](#insn-00baf4c4)
- ブロック [`00baf4c4`](#insn-00baf4c4) 範囲 `[['00baf4c4', '00baf4c7']]`
  - `UNCONDITIONAL_JUMP` [`00baf4c4`](#insn-00baf4c4) → [`00baf460`](#insn-00baf460)
- ブロック [`00baf4c8`](#insn-00baf4c8) 範囲 `[['00baf4c8', '00baf4df']]`
  - `FALL_THROUGH` [`00baf4dc`](#insn-00baf4dc) → [`00baf4e0`](#insn-00baf4e0)
- ブロック [`00baf4e0`](#insn-00baf4e0) 範囲 `[['00baf4e0', '00baf503']]`

## 命令位置別の参照

- [`00baf2b4`](#insn-00baf2b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2b8`](#insn-00baf2b8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2bc`](#insn-00baf2bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2c0`](#insn-00baf2c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2d4`](#insn-00baf2d4) → `002a568a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2dc`](#insn-00baf2dc) → [`00bde8d0`](../00bde/00bde8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde8d0` · 推定シンボル `None` · 推定型 `None`
- [`00baf2e0`](#insn-00baf2e0) → [`00baf474`](#insn-00baf474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2f0`](#insn-00baf2f0) → [`00be1470`](../00be1/00be1470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1470` · 推定シンボル `None` · 推定型 `None`
- [`00baf2f4`](#insn-00baf2f4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf2f8`](#insn-00baf2f8) → [`00baf4c8`](#insn-00baf4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf300`](#insn-00baf300) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf308`](#insn-00baf308) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf30c`](#insn-00baf30c) → [`00be1b80`](../00be1/00be1b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b80` · 推定シンボル `None` · 推定型 `None`
- [`00baf314`](#insn-00baf314) → [`00baf320`](#insn-00baf320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf31c`](#insn-00baf31c) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf328`](#insn-00baf328) → [`00baf3c0`](#insn-00baf3c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf330`](#insn-00baf330) → [`00baf3bc`](#insn-00baf3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf338`](#insn-00baf338) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf33c`](#insn-00baf33c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00baf348`](#insn-00baf348) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf350`](#insn-00baf350) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf364`](#insn-00baf364) → [`00be1a70`](../00be1/00be1a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a70` · 推定シンボル `None` · 推定型 `None`
- [`00baf36c`](#insn-00baf36c) → [`00baf378`](#insn-00baf378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf374`](#insn-00baf374) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf37c`](#insn-00baf37c) → [`00baf3c0`](#insn-00baf3c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf380`](#insn-00baf380) → `Stack[-0x44]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf388`](#insn-00baf388) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf390`](#insn-00baf390) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf398`](#insn-00baf398) → [`00be1a10`](../00be1/00be1a10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a10` · 推定シンボル `None` · 推定型 `None`
- [`00baf3a0`](#insn-00baf3a0) → [`00baf3ac`](#insn-00baf3ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3a8`](#insn-00baf3a8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf3b0`](#insn-00baf3b0) → [`00baf490`](#insn-00baf490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3b8`](#insn-00baf3b8) → [`00baf3c0`](#insn-00baf3c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3c8`](#insn-00baf3c8) → [`00baf460`](#insn-00baf460) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3d0`](#insn-00baf3d0) → [`00baf45c`](#insn-00baf45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3d8`](#insn-00baf3d8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf3dc`](#insn-00baf3dc) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00baf3e8`](#insn-00baf3e8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf3f0`](#insn-00baf3f0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf404`](#insn-00baf404) → [`00be1a70`](../00be1/00be1a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a70` · 推定シンボル `None` · 推定型 `None`
- [`00baf40c`](#insn-00baf40c) → [`00baf418`](#insn-00baf418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf414`](#insn-00baf414) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf41c`](#insn-00baf41c) → [`00baf460`](#insn-00baf460) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf420`](#insn-00baf420) → `Stack[-0x44]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf428`](#insn-00baf428) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf430`](#insn-00baf430) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf438`](#insn-00baf438) → [`00be1a10`](../00be1/00be1a10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a10` · 推定シンボル `None` · 推定型 `None`
- [`00baf440`](#insn-00baf440) → [`00baf44c`](#insn-00baf44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf448`](#insn-00baf448) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baf450`](#insn-00baf450) → [`00baf4ac`](#insn-00baf4ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf458`](#insn-00baf458) → [`00baf460`](#insn-00baf460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf468`](#insn-00baf468) → [`00b7501c`](../00b75/00b7501c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b7501c` · 推定シンボル `None` · 推定型 `None`
- [`00baf470`](#insn-00baf470) → [`00be1830`](../00be1/00be1830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1830` · 推定シンボル `None` · 推定型 `None`
- [`00baf474`](#insn-00baf474) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf478`](#insn-00baf478) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf47c`](#insn-00baf47c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf480`](#insn-00baf480) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf49c`](#insn-00baf49c) → [`00baf3b4`](#insn-00baf3b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4a4`](#insn-00baf4a4) → [`00baf3b4`](#insn-00baf3b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4a8`](#insn-00baf4a8) → [`00baf3c0`](#insn-00baf3c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4b8`](#insn-00baf4b8) → [`00baf454`](#insn-00baf454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4c0`](#insn-00baf4c0) → [`00baf454`](#insn-00baf454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4c4`](#insn-00baf4c4) → [`00baf460`](#insn-00baf460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4d0`](#insn-00baf4d0) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00baf4d8`](#insn-00baf4d8) → `0029999a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00baf4e8`](#insn-00baf4e8) → [`00ba89b8`](../00ba8/00ba89b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba89b8` · 推定シンボル `None` · 推定型 `None`
- [`00baf4ec`](#insn-00baf4ec) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4f0`](#insn-00baf4f0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf4fc`](#insn-00baf4fc) → [`00be0eb0`](../00be0/00be0eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0eb0` · 推定シンボル `None` · 推定型 `None`
- [`00baf500`](#insn-00baf500) → [`0041e0fc`](../0041e/0041e0fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e0fc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf2b4`](#insn-00baf2b4)

~~~json
{
  "source": "00baf2b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2b8`](#insn-00baf2b8)

~~~json
{
  "source": "00baf2b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2bc`](#insn-00baf2bc)

~~~json
{
  "source": "00baf2bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2c0`](#insn-00baf2c0)

~~~json
{
  "source": "00baf2c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2d4`](#insn-00baf2d4)

~~~json
{
  "source": "00baf2d4",
  "target": "002a568a",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2dc`](#insn-00baf2dc)

~~~json
{
  "source": "00baf2dc",
  "target": "00bde8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf2e0`](#insn-00baf2e0)

~~~json
{
  "source": "00baf2e0",
  "target": "00baf474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2f0`](#insn-00baf2f0)

~~~json
{
  "source": "00baf2f0",
  "target": "00be1470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf2f4`](#insn-00baf2f4)

~~~json
{
  "source": "00baf2f4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf2f8`](#insn-00baf2f8)

~~~json
{
  "source": "00baf2f8",
  "target": "00baf4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf300`](#insn-00baf300)

~~~json
{
  "source": "00baf300",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf308`](#insn-00baf308)

~~~json
{
  "source": "00baf308",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf30c`](#insn-00baf30c)

~~~json
{
  "source": "00baf30c",
  "target": "00be1b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf314`](#insn-00baf314)

~~~json
{
  "source": "00baf314",
  "target": "00baf320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf31c`](#insn-00baf31c)

~~~json
{
  "source": "00baf31c",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf328`](#insn-00baf328)

~~~json
{
  "source": "00baf328",
  "target": "00baf3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf330`](#insn-00baf330)

~~~json
{
  "source": "00baf330",
  "target": "00baf3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf338`](#insn-00baf338)

~~~json
{
  "source": "00baf338",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf33c`](#insn-00baf33c)

~~~json
{
  "source": "00baf33c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf348`](#insn-00baf348)

~~~json
{
  "source": "00baf348",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf350`](#insn-00baf350)

~~~json
{
  "source": "00baf350",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf364`](#insn-00baf364)

~~~json
{
  "source": "00baf364",
  "target": "00be1a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf36c`](#insn-00baf36c)

~~~json
{
  "source": "00baf36c",
  "target": "00baf378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf374`](#insn-00baf374)

~~~json
{
  "source": "00baf374",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf37c`](#insn-00baf37c)

~~~json
{
  "source": "00baf37c",
  "target": "00baf3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf380`](#insn-00baf380)

~~~json
{
  "source": "00baf380",
  "target": "Stack[-0x44]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf388`](#insn-00baf388)

~~~json
{
  "source": "00baf388",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf390`](#insn-00baf390)

~~~json
{
  "source": "00baf390",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf398`](#insn-00baf398)

~~~json
{
  "source": "00baf398",
  "target": "00be1a10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf3a0`](#insn-00baf3a0)

~~~json
{
  "source": "00baf3a0",
  "target": "00baf3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3a8`](#insn-00baf3a8)

~~~json
{
  "source": "00baf3a8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf3b0`](#insn-00baf3b0)

~~~json
{
  "source": "00baf3b0",
  "target": "00baf490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3b8`](#insn-00baf3b8)

~~~json
{
  "source": "00baf3b8",
  "target": "00baf3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3c8`](#insn-00baf3c8)

~~~json
{
  "source": "00baf3c8",
  "target": "00baf460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3d0`](#insn-00baf3d0)

~~~json
{
  "source": "00baf3d0",
  "target": "00baf45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3d8`](#insn-00baf3d8)

~~~json
{
  "source": "00baf3d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf3dc`](#insn-00baf3dc)

~~~json
{
  "source": "00baf3dc",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf3e8`](#insn-00baf3e8)

~~~json
{
  "source": "00baf3e8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf3f0`](#insn-00baf3f0)

~~~json
{
  "source": "00baf3f0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf404`](#insn-00baf404)

~~~json
{
  "source": "00baf404",
  "target": "00be1a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf40c`](#insn-00baf40c)

~~~json
{
  "source": "00baf40c",
  "target": "00baf418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf414`](#insn-00baf414)

~~~json
{
  "source": "00baf414",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf41c`](#insn-00baf41c)

~~~json
{
  "source": "00baf41c",
  "target": "00baf460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf420`](#insn-00baf420)

~~~json
{
  "source": "00baf420",
  "target": "Stack[-0x44]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf428`](#insn-00baf428)

~~~json
{
  "source": "00baf428",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf430`](#insn-00baf430)

~~~json
{
  "source": "00baf430",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf438`](#insn-00baf438)

~~~json
{
  "source": "00baf438",
  "target": "00be1a10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf440`](#insn-00baf440)

~~~json
{
  "source": "00baf440",
  "target": "00baf44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf448`](#insn-00baf448)

~~~json
{
  "source": "00baf448",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf450`](#insn-00baf450)

~~~json
{
  "source": "00baf450",
  "target": "00baf4ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf458`](#insn-00baf458)

~~~json
{
  "source": "00baf458",
  "target": "00baf460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf468`](#insn-00baf468)

~~~json
{
  "source": "00baf468",
  "target": "00b7501c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf470`](#insn-00baf470)

~~~json
{
  "source": "00baf470",
  "target": "00be1830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf474`](#insn-00baf474)

~~~json
{
  "source": "00baf474",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf478`](#insn-00baf478)

~~~json
{
  "source": "00baf478",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf47c`](#insn-00baf47c)

~~~json
{
  "source": "00baf47c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf480`](#insn-00baf480)

~~~json
{
  "source": "00baf480",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf49c`](#insn-00baf49c)

~~~json
{
  "source": "00baf49c",
  "target": "00baf3b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4a4`](#insn-00baf4a4)

~~~json
{
  "source": "00baf4a4",
  "target": "00baf3b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4a8`](#insn-00baf4a8)

~~~json
{
  "source": "00baf4a8",
  "target": "00baf3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4b8`](#insn-00baf4b8)

~~~json
{
  "source": "00baf4b8",
  "target": "00baf454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4c0`](#insn-00baf4c0)

~~~json
{
  "source": "00baf4c0",
  "target": "00baf454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4c4`](#insn-00baf4c4)

~~~json
{
  "source": "00baf4c4",
  "target": "00baf460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4d0`](#insn-00baf4d0)

~~~json
{
  "source": "00baf4d0",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf4d8`](#insn-00baf4d8)

~~~json
{
  "source": "00baf4d8",
  "target": "0029999a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029999a",
  "offset": 0,
  "size": 64,
  "datatype": "string",
  "bytes": "6e756d70756e63745f62796e616d653c636861723e3a3a6e756d70756e63745f",
  "capture_start": "0029999a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00baf4e8`](#insn-00baf4e8)

~~~json
{
  "source": "00baf4e8",
  "target": "00ba89b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf4ec`](#insn-00baf4ec)

~~~json
{
  "source": "00baf4ec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4f0`](#insn-00baf4f0)

~~~json
{
  "source": "00baf4f0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf4fc`](#insn-00baf4fc)

~~~json
{
  "source": "00baf4fc",
  "target": "00be0eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf500`](#insn-00baf500)

~~~json
{
  "source": "00baf500",
  "target": "0041e0fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
