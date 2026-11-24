# 00afda0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afca18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afca18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-73a4a3a7867729733f4ac7968ea3bd35)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afda0c",
  "name": "FUN_00afda0c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e393149512a81e6017562975e813c2b5d45ec37e887727ac144c1ef64bcc080",
  "source_text_sha256": "7e393149512a81e6017562975e813c2b5d45ec37e887727ac144c1ef64bcc080",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afda0c",
        "00afda57"
      ]
    ],
    "bytes_sha256": "9b495b232abd8de4cdce8187c2c8a986c7459a878e32d1589e404c629b301974",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)
- [00717198](../00717/00717198.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 565 bytes

~~~c

void FUN_00afda0c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afd478 with catch @ 00afda10 */
                    /* catch() { ... } // from try @ 00afd364 with catch @ 00afda14 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd254 with catch @ 00afda30 */
                    /* catch() { ... } // from try @ 00afd138 with catch @ 00afda34 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc4) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afda0c"></a> `00afda0c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afda10"></a> `00afda10` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afda14"></a> `00afda14` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afda18"></a> `00afda18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afda1c"></a> `00afda1c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afda20"></a> `00afda20` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afda24"></a> `00afda24` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afda28"></a> `00afda28` | `b5 52 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afda2c"></a> `00afda2c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afda30"></a> `00afda30` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afda34"></a> `00afda34` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afda38"></a> `00afda38` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afda3c"></a> `00afda3c` | `89 78 89 52` | mov w9,#0x4bc4 | `FALL_THROUGH`
<a id="insn-00afda40"></a> `00afda40` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afda44"></a> `00afda44` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afda48"></a> `00afda48` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afda4c"></a> `00afda4c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afda50"></a> `00afda50` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afda54"></a> `00afda54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afda0c`](#insn-00afda0c) 範囲 `[['00afda0c', '00afda0f']]`
  - `FALL_THROUGH` [`00afda0c`](#insn-00afda0c) → [`00afda10`](#insn-00afda10)
- ブロック [`00afda10`](#insn-00afda10) 範囲 `[['00afda10', '00afda13']]`
  - `FALL_THROUGH` [`00afda10`](#insn-00afda10) → [`00afda14`](#insn-00afda14)
- ブロック [`00afda14`](#insn-00afda14) 範囲 `[['00afda14', '00afda2f']]`
  - `FALL_THROUGH` [`00afda2c`](#insn-00afda2c) → [`00afda30`](#insn-00afda30)
- ブロック [`00afda30`](#insn-00afda30) 範囲 `[['00afda30', '00afda33']]`
  - `FALL_THROUGH` [`00afda30`](#insn-00afda30) → [`00afda34`](#insn-00afda34)
- ブロック [`00afda34`](#insn-00afda34) 範囲 `[['00afda34', '00afda57']]`

## 命令位置別の参照

- [`00afda0c`](#insn-00afda0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda10`](#insn-00afda10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda14`](#insn-00afda14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda28`](#insn-00afda28) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afda48`](#insn-00afda48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda4c`](#insn-00afda4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afda50`](#insn-00afda50) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afda0c`](#insn-00afda0c)

~~~json
{
  "source": "00afda0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda10`](#insn-00afda10)

~~~json
{
  "source": "00afda10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda14`](#insn-00afda14)

~~~json
{
  "source": "00afda14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda28`](#insn-00afda28)

~~~json
{
  "source": "00afda28",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afda48`](#insn-00afda48)

~~~json
{
  "source": "00afda48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda4c`](#insn-00afda4c)

~~~json
{
  "source": "00afda4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afda50`](#insn-00afda50)

~~~json
{
  "source": "00afda50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
