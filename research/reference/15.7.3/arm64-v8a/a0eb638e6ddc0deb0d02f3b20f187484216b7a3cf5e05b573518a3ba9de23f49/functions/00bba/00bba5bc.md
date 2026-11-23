# 00bba5bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba4f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba4f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-4c93806776bd17a7212ca8178e7f85b3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bba600`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba600.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0024.md#compare-682d12cb26a23212c5d3c975681c00d7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba5bc",
  "name": "_ZNKSt6__ndk123__match_any_but_newlineIwE6__execERNS_7__stateIwEE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab81cbe61f80fb3a41288b0678162b3f7737237f3273286d7d8fe08bb76a2f6d",
  "source_text_sha256": "ab81cbe61f80fb3a41288b0678162b3f7737237f3273286d7d8fe08bb76a2f6d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bba5bc",
        "00bba613"
      ]
    ],
    "bytes_sha256": "a7144b7724aa47f62d9257897ac4999d7120fa5cbf16b5199a05e4bc999226fa",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1018 bytes

~~~c

void _ZNKSt6__ndk123__match_any_but_newlineIwE6__execERNS_7__stateIwEE
               (long param_1,undefined4 *param_2)

{
  int *piVar1;
  int iVar2;
  undefined8 uVar3;
  
  piVar1 = *(int **)(param_2 + 4);
                    /* catch() { ... } // from try @ 00bb7988 with catch @ 00bba5c4 */
                    /* catch() { ... } // from try @ 00bb797c with catch @ 00bba5d8 */
                    /* catch() { ... } // from try @ 00bb78e8 with catch @ 00bba5dc */
  if ((piVar1 != *(int **)(param_2 + 6)) &&
     (iVar2 = *piVar1, (1 < iVar2 - 0x2028U && iVar2 != 0xd) && iVar2 != 10)) {
    uVar3 = *(undefined8 *)(param_1 + 8);
    *param_2 = 0xfffffc1d;
    *(int **)(param_2 + 4) = piVar1 + 1;
                    /* catch() { ... } // from try @ 00bb78cc with catch @ 00bba60c */
    *(undefined8 *)(param_2 + 0x14) = uVar3;
    return;
  }
  *(undefined8 *)(param_2 + 0x14) = 0;
  *param_2 = 0xfffffc1f;
                    /* catch() { ... } // from try @ 00bb78d8 with catch @ 00bba5f4 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bba5bc"></a> `00bba5bc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bba5c0"></a> `00bba5c0` | `28 24 41 a9` | ldp x8,x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bba5c4"></a> `00bba5c4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bba5c8"></a> `00bba5c8` | `00 01 00 54` | b.eq 0x00bba5e8 | `CONDITIONAL_JUMP`
<a id="insn-00bba5cc"></a> `00bba5cc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bba5d0"></a> `00bba5d0` | `ea 04 84 12` | mov w10,#0xffffdfd8 | `FALL_THROUGH`
<a id="insn-00bba5d4"></a> `00bba5d4` | `2a 01 0a 0b` | add w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00bba5d8"></a> `00bba5d8` | `5f 09 00 71` | cmp w10,#0x2 | `FALL_THROUGH`
<a id="insn-00bba5dc"></a> `00bba5dc` | `24 29 4d 7a` | ccmp w9,#0xd,#0x4,cs | `FALL_THROUGH`
<a id="insn-00bba5e0"></a> `00bba5e0` | `24 19 4a 7a` | ccmp w9,#0xa,#0x4,ne | `FALL_THROUGH`
<a id="insn-00bba5e4"></a> `00bba5e4` | `a1 00 00 54` | b.ne 0x00bba5f8 | `CONDITIONAL_JUMP`
<a id="insn-00bba5e8"></a> `00bba5e8` | `09 7c 80 12` | mov w9,#0xfffffc1f | `FALL_THROUGH`
<a id="insn-00bba5ec"></a> `00bba5ec` | `3f 28 00 f9` | str xzr,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bba5f0"></a> `00bba5f0` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bba5f4"></a> `00bba5f4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bba5f8"></a> `00bba5f8` | `0a 11 00 91` | add x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bba5fc"></a> `00bba5fc` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bba600"></a> `00bba600` | `49 7c 80 12` | mov w9,#0xfffffc1d | `FALL_THROUGH`
<a id="insn-00bba604"></a> `00bba604` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bba608"></a> `00bba608` | `2a 08 00 f9` | str x10,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bba60c"></a> `00bba60c` | `28 28 00 f9` | str x8,[x1, #0x50] | `FALL_THROUGH`
<a id="insn-00bba610"></a> `00bba610` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bba5bc`](#insn-00bba5bc) 範囲 `[['00bba5bc', '00bba5c3']]`
  - `FALL_THROUGH` [`00bba5c0`](#insn-00bba5c0) → [`00bba5c4`](#insn-00bba5c4)
- ブロック [`00bba5c4`](#insn-00bba5c4) 範囲 `[['00bba5c4', '00bba5cb']]`
  - `CONDITIONAL_JUMP` [`00bba5c8`](#insn-00bba5c8) → [`00bba5e8`](#insn-00bba5e8)
  - `FALL_THROUGH` [`00bba5c8`](#insn-00bba5c8) → [`00bba5cc`](#insn-00bba5cc)
- ブロック [`00bba5cc`](#insn-00bba5cc) 範囲 `[['00bba5cc', '00bba5d7']]`
  - `FALL_THROUGH` [`00bba5d4`](#insn-00bba5d4) → [`00bba5d8`](#insn-00bba5d8)
- ブロック [`00bba5d8`](#insn-00bba5d8) 範囲 `[['00bba5d8', '00bba5db']]`
  - `FALL_THROUGH` [`00bba5d8`](#insn-00bba5d8) → [`00bba5dc`](#insn-00bba5dc)
- ブロック [`00bba5dc`](#insn-00bba5dc) 範囲 `[['00bba5dc', '00bba5e7']]`
  - `CONDITIONAL_JUMP` [`00bba5e4`](#insn-00bba5e4) → [`00bba5f8`](#insn-00bba5f8)
  - `FALL_THROUGH` [`00bba5e4`](#insn-00bba5e4) → [`00bba5e8`](#insn-00bba5e8)
- ブロック [`00bba5e8`](#insn-00bba5e8) 範囲 `[['00bba5e8', '00bba5f3']]`
  - `FALL_THROUGH` [`00bba5f0`](#insn-00bba5f0) → [`00bba5f4`](#insn-00bba5f4)
- ブロック [`00bba5f4`](#insn-00bba5f4) 範囲 `[['00bba5f4', '00bba5f7']]`
- ブロック [`00bba5f8`](#insn-00bba5f8) 範囲 `[['00bba5f8', '00bba60b']]`
  - `FALL_THROUGH` [`00bba608`](#insn-00bba608) → [`00bba60c`](#insn-00bba60c)
- ブロック [`00bba60c`](#insn-00bba60c) 範囲 `[['00bba60c', '00bba613']]`

## 命令位置別の参照

- [`00bba5c8`](#insn-00bba5c8) → [`00bba5e8`](#insn-00bba5e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bba5e4`](#insn-00bba5e4) → [`00bba5f8`](#insn-00bba5f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bba5c8`](#insn-00bba5c8)

~~~json
{
  "source": "00bba5c8",
  "target": "00bba5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bba5e4`](#insn-00bba5e4)

~~~json
{
  "source": "00bba5e4",
  "target": "00bba5f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
