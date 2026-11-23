# 00babb5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00babc24`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babc24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-e6d65808832668c775500c879f025ad2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babb5c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d17161b59f99e7ffe525def48afae8fe7b5d98e5cd06bceac57d432a55e2a3cc",
  "source_text_sha256": "d17161b59f99e7ffe525def48afae8fe7b5d98e5cd06bceac57d432a55e2a3cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babb5c",
        "00babc3b"
      ]
    ],
    "bytes_sha256": "c269d6f510503f8beeab3ab518ecfed068a93ab98f92bd3a593a127f25b2bc90",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1aa0](../00be1/00be1aa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1479 bytes

~~~c

int _ZNKSt6__ndk17codecvtIwc9mbstate_tE9do_lengthERS1_PKcS5_m
              (long param_1,mbstate_t *param_2,char *param_3,char *param_4,ulong param_5)

{
  __locale_t __dataset;
  size_t sVar1;
  int iVar2;
  int iVar3;
  ulong uVar4;
  
                    /* try { // try from 00babb68 to 00cabb7f has its CatchHandler @ 00babbd0 */
  iVar3 = 0;
                    /* try { // try from 00babb80 to 00cabd3b has its CatchHandler @ 00bab67c */
  if ((param_5 != 0) && (param_3 != param_4)) {
    iVar3 = 0;
    uVar4 = 1;
    do {
      __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
      sVar1 = mbrlen(param_3,(long)param_4 - (long)param_3,param_2);
                    /* catch() { ... } // from try @ 00babb68 with catch @ 00babbd0 */
      if (__dataset != (__locale_t)0x0) {
        uselocale(__dataset);
      }
      if (sVar1 == 0) {
        sVar1 = 1;
        iVar2 = 1;
      }
      else {
                    /* catch() { ... } // from try @ 00babb58 with catch @ 00babbe8 */
        if (sVar1 + 2 < 2) {
          return iVar3;
        }
        iVar2 = (int)sVar1;
      }
                    /* catch() { ... } // from try @ 00baba44 with catch @ 00babbfc */
      iVar3 = iVar2 + iVar3;
      if (param_5 <= uVar4) {
        return iVar3;
      }
      param_3 = param_3 + sVar1;
      uVar4 = uVar4 + 1;
    } while (param_3 != param_4);
  }
                    /* catch() { ... } // from try @ 00bab8c8 with catch @ 00babc18 */
  return iVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babb5c"></a> `00babb5c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00babb60"></a> `00babb60` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00babb64"></a> `00babb64` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb68"></a> `00babb68` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb6c"></a> `00babb6c` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babb70"></a> `00babb70` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babb74"></a> `00babb74` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babb78"></a> `00babb78` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00babb7c"></a> `00babb7c` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00babb80"></a> `00babb80` | `c4 04 00 b4` | cbz x4,0x00babc18 | `CONDITIONAL_JUMP`
<a id="insn-00babb84"></a> `00babb84` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00babb88"></a> `00babb88` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00babb8c"></a> `00babb8c` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00babb90"></a> `00babb90` | `40 04 00 54` | b.eq 0x00babc18 | `CONDITIONAL_JUMP`
<a id="insn-00babb94"></a> `00babb94` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00babb98"></a> `00babb98` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00babb9c"></a> `00babb9c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00babba0"></a> `00babba0` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00babba4"></a> `00babba4` | `3b 00 80 52` | mov w27,#0x1 | `FALL_THROUGH`
<a id="insn-00babba8"></a> `00babba8` | `00 0b 40 f9` | ldr x0,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00babbac"></a> `00babbac` | `b9 02 16 cb` | sub x25,x21,x22 | `FALL_THROUGH`
<a id="insn-00babbb0"></a> `00babbb0` | `34 d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babbb4"></a> `00babbb4` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00babbb8"></a> `00babbb8` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00babbbc"></a> `00babbbc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00babbc0"></a> `00babbc0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00babbc4"></a> `00babbc4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00babbc8"></a> `00babbc8` | `b6 d7 00 94` | bl 0x00be1aa0 | `UNCONDITIONAL_CALL`
<a id="insn-00babbcc"></a> `00babbcc` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00babbd0"></a> `00babbd0` | `7a 00 00 b4` | cbz x26,0x00babbdc | `CONDITIONAL_JUMP`
<a id="insn-00babbd4"></a> `00babbd4` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00babbd8"></a> `00babbd8` | `2a d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babbdc"></a> `00babbdc` | `d9 00 00 b4` | cbz x25,0x00babbf4 | `CONDITIONAL_JUMP`
<a id="insn-00babbe0"></a> `00babbe0` | `28 0b 00 91` | add x8,x25,#0x2 | `FALL_THROUGH`
<a id="insn-00babbe4"></a> `00babbe4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00babbe8"></a> `00babbe8` | `83 01 00 54` | b.cc 0x00babc18 | `CONDITIONAL_JUMP`
<a id="insn-00babbec"></a> `00babbec` | `e8 03 19 2a` | mov w8,w25 | `FALL_THROUGH`
<a id="insn-00babbf0"></a> `00babbf0` | `03 00 00 14` | b 0x00babbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00babbf4"></a> `00babbf4` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00babbf8"></a> `00babbf8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00babbfc"></a> `00babbfc` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00babc00"></a> `00babc00` | `13 01 13 0b` | add w19,w8,w19 | `FALL_THROUGH`
<a id="insn-00babc04"></a> `00babc04` | `a2 00 00 54` | b.cs 0x00babc18 | `CONDITIONAL_JUMP`
<a id="insn-00babc08"></a> `00babc08` | `d6 02 19 8b` | add x22,x22,x25 | `FALL_THROUGH`
<a id="insn-00babc0c"></a> `00babc0c` | `7b 07 00 91` | add x27,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00babc10"></a> `00babc10` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00babc14"></a> `00babc14` | `a1 fc ff 54` | b.ne 0x00babba8 | `CONDITIONAL_JUMP`
<a id="insn-00babc18"></a> `00babc18` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00babc1c"></a> `00babc1c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babc20"></a> `00babc20` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babc24"></a> `00babc24` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babc28"></a> `00babc28` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babc2c"></a> `00babc2c` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babc30"></a> `00babc30` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00babc34"></a> `00babc34` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00babc38"></a> `00babc38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babb5c`](#insn-00babb5c) 範囲 `[['00babb5c', '00babb67']]`
  - `FALL_THROUGH` [`00babb64`](#insn-00babb64) → [`00babb68`](#insn-00babb68)
- ブロック [`00babb68`](#insn-00babb68) 範囲 `[['00babb68', '00babb7f']]`
  - `FALL_THROUGH` [`00babb7c`](#insn-00babb7c) → [`00babb80`](#insn-00babb80)
- ブロック [`00babb80`](#insn-00babb80) 範囲 `[['00babb80', '00babb83']]`
  - `CONDITIONAL_JUMP` [`00babb80`](#insn-00babb80) → [`00babc18`](#insn-00babc18)
  - `FALL_THROUGH` [`00babb80`](#insn-00babb80) → [`00babb84`](#insn-00babb84)
- ブロック [`00babb84`](#insn-00babb84) 範囲 `[['00babb84', '00babb93']]`
  - `CONDITIONAL_JUMP` [`00babb90`](#insn-00babb90) → [`00babc18`](#insn-00babc18)
  - `FALL_THROUGH` [`00babb90`](#insn-00babb90) → [`00babb94`](#insn-00babb94)
- ブロック [`00babb94`](#insn-00babb94) 範囲 `[['00babb94', '00babba7']]`
  - `FALL_THROUGH` [`00babba4`](#insn-00babba4) → [`00babba8`](#insn-00babba8)
- ブロック [`00babba8`](#insn-00babba8) 範囲 `[['00babba8', '00babbcf']]`
  - `FALL_THROUGH` [`00babbcc`](#insn-00babbcc) → [`00babbd0`](#insn-00babbd0)
- ブロック [`00babbd0`](#insn-00babbd0) 範囲 `[['00babbd0', '00babbd3']]`
  - `CONDITIONAL_JUMP` [`00babbd0`](#insn-00babbd0) → [`00babbdc`](#insn-00babbdc)
  - `FALL_THROUGH` [`00babbd0`](#insn-00babbd0) → [`00babbd4`](#insn-00babbd4)
- ブロック [`00babbd4`](#insn-00babbd4) 範囲 `[['00babbd4', '00babbdb']]`
  - `FALL_THROUGH` [`00babbd8`](#insn-00babbd8) → [`00babbdc`](#insn-00babbdc)
- ブロック [`00babbdc`](#insn-00babbdc) 範囲 `[['00babbdc', '00babbdf']]`
  - `CONDITIONAL_JUMP` [`00babbdc`](#insn-00babbdc) → [`00babbf4`](#insn-00babbf4)
  - `FALL_THROUGH` [`00babbdc`](#insn-00babbdc) → [`00babbe0`](#insn-00babbe0)
- ブロック [`00babbe0`](#insn-00babbe0) 範囲 `[['00babbe0', '00babbe7']]`
  - `FALL_THROUGH` [`00babbe4`](#insn-00babbe4) → [`00babbe8`](#insn-00babbe8)
- ブロック [`00babbe8`](#insn-00babbe8) 範囲 `[['00babbe8', '00babbeb']]`
  - `CONDITIONAL_JUMP` [`00babbe8`](#insn-00babbe8) → [`00babc18`](#insn-00babc18)
  - `FALL_THROUGH` [`00babbe8`](#insn-00babbe8) → [`00babbec`](#insn-00babbec)
- ブロック [`00babbec`](#insn-00babbec) 範囲 `[['00babbec', '00babbf3']]`
  - `UNCONDITIONAL_JUMP` [`00babbf0`](#insn-00babbf0) → [`00babbfc`](#insn-00babbfc)
- ブロック [`00babbf4`](#insn-00babbf4) 範囲 `[['00babbf4', '00babbfb']]`
  - `FALL_THROUGH` [`00babbf8`](#insn-00babbf8) → [`00babbfc`](#insn-00babbfc)
- ブロック [`00babbfc`](#insn-00babbfc) 範囲 `[['00babbfc', '00babc07']]`
  - `CONDITIONAL_JUMP` [`00babc04`](#insn-00babc04) → [`00babc18`](#insn-00babc18)
  - `FALL_THROUGH` [`00babc04`](#insn-00babc04) → [`00babc08`](#insn-00babc08)
- ブロック [`00babc08`](#insn-00babc08) 範囲 `[['00babc08', '00babc17']]`
  - `CONDITIONAL_JUMP` [`00babc14`](#insn-00babc14) → [`00babba8`](#insn-00babba8)
  - `FALL_THROUGH` [`00babc14`](#insn-00babc14) → [`00babc18`](#insn-00babc18)
- ブロック [`00babc18`](#insn-00babc18) 範囲 `[['00babc18', '00babc3b']]`

## 命令位置別の参照

- [`00babb60`](#insn-00babb60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb64`](#insn-00babb64) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb68`](#insn-00babb68) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb6c`](#insn-00babb6c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb70`](#insn-00babb70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb74`](#insn-00babb74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb80`](#insn-00babb80) → [`00babc18`](#insn-00babc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb90`](#insn-00babb90) → [`00babc18`](#insn-00babc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babbb0`](#insn-00babbb0) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babbb8`](#insn-00babbb8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babbc8`](#insn-00babbc8) → [`00be1aa0`](../00be1/00be1aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1aa0` · 推定シンボル `None` · 推定型 `None`
- [`00babbd0`](#insn-00babbd0) → [`00babbdc`](#insn-00babbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babbd8`](#insn-00babbd8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babbdc`](#insn-00babbdc) → [`00babbf4`](#insn-00babbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babbe8`](#insn-00babbe8) → [`00babc18`](#insn-00babc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babbf0`](#insn-00babbf0) → [`00babbfc`](#insn-00babbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc04`](#insn-00babc04) → [`00babc18`](#insn-00babc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc14`](#insn-00babc14) → [`00babba8`](#insn-00babba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc1c`](#insn-00babc1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc20`](#insn-00babc20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc24`](#insn-00babc24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc28`](#insn-00babc28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc2c`](#insn-00babc2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc30`](#insn-00babc30) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babb60`](#insn-00babb60)

~~~json
{
  "source": "00babb60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb64`](#insn-00babb64)

~~~json
{
  "source": "00babb64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb68`](#insn-00babb68)

~~~json
{
  "source": "00babb68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb6c`](#insn-00babb6c)

~~~json
{
  "source": "00babb6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb70`](#insn-00babb70)

~~~json
{
  "source": "00babb70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb74`](#insn-00babb74)

~~~json
{
  "source": "00babb74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb80`](#insn-00babb80)

~~~json
{
  "source": "00babb80",
  "target": "00babc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb90`](#insn-00babb90)

~~~json
{
  "source": "00babb90",
  "target": "00babc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babbb0`](#insn-00babbb0)

~~~json
{
  "source": "00babbb0",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babbb8`](#insn-00babbb8)

~~~json
{
  "source": "00babbb8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babbc8`](#insn-00babbc8)

~~~json
{
  "source": "00babbc8",
  "target": "00be1aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babbd0`](#insn-00babbd0)

~~~json
{
  "source": "00babbd0",
  "target": "00babbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babbd8`](#insn-00babbd8)

~~~json
{
  "source": "00babbd8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babbdc`](#insn-00babbdc)

~~~json
{
  "source": "00babbdc",
  "target": "00babbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babbe8`](#insn-00babbe8)

~~~json
{
  "source": "00babbe8",
  "target": "00babc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babbf0`](#insn-00babbf0)

~~~json
{
  "source": "00babbf0",
  "target": "00babbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc04`](#insn-00babc04)

~~~json
{
  "source": "00babc04",
  "target": "00babc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc14`](#insn-00babc14)

~~~json
{
  "source": "00babc14",
  "target": "00babba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc1c`](#insn-00babc1c)

~~~json
{
  "source": "00babc1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc20`](#insn-00babc20)

~~~json
{
  "source": "00babc20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc24`](#insn-00babc24)

~~~json
{
  "source": "00babc24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc28`](#insn-00babc28)

~~~json
{
  "source": "00babc28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc2c`](#insn-00babc2c)

~~~json
{
  "source": "00babc2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc30`](#insn-00babc30)

~~~json
{
  "source": "00babc30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
