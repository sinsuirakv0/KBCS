# 00afae4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9e58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9e58.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-f38a47cce08e2deec1939553917b7578)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afae4c",
  "name": "FUN_00afae4c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ee27bd8fcc2229d4de27830353f66ac2c5b9de74bc40608f4761fc7102e39d9",
  "source_text_sha256": "4ee27bd8fcc2229d4de27830353f66ac2c5b9de74bc40608f4761fc7102e39d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afae4c",
        "00afaebb"
      ]
    ],
    "bytes_sha256": "671904d6b607d9bf2343aed4c2db1acb07cba968a558e8ba1afa9536d3a70444",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 559 bytes

~~~c

bool FUN_00afae4c(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008524fc();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) != 0;
  }
                    /* catch() { ... } // from try @ 00afae40 with catch @ 00afaeb4 */
                    /* catch() { ... } // from try @ 00afadac with catch @ 00afaeb8 */
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afae4c"></a> `00afae4c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afae50"></a> `00afae50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afae54"></a> `00afae54` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afae58"></a> `00afae58` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afae5c"></a> `00afae5c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afae60"></a> `00afae60` | `a7 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afae64"></a> `00afae64` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afae68"></a> `00afae68` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afae6c"></a> `00afae6c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afae70"></a> `00afae70` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afae74"></a> `00afae74` | `67 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afae78"></a> `00afae78` | `60 00 00 37` | tbnz w0,#0x0,0x00afae84 | `CONDITIONAL_JUMP`
<a id="insn-00afae7c"></a> `00afae7c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afae80"></a> `00afae80` | `0c 00 00 14` | b 0x00afaeb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afae84"></a> `00afae84` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afae88"></a> `00afae88` | `9d 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afae8c"></a> `00afae8c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afae90"></a> `00afae90` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afae94"></a> `00afae94` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afae98"></a> `00afae98` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afae9c"></a> `00afae9c` | `89 61 89 52` | mov w9,#0x4b0c | `FALL_THROUGH`
<a id="insn-00afaea0"></a> `00afaea0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaea4"></a> `00afaea4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaea8"></a> `00afaea8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afaeac"></a> `00afaeac` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afaeb0"></a> `00afaeb0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaeb4"></a> `00afaeb4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afaeb8"></a> `00afaeb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afae4c`](#insn-00afae4c) 範囲 `[['00afae4c', '00afae7b']]`
  - `CONDITIONAL_JUMP` [`00afae78`](#insn-00afae78) → [`00afae84`](#insn-00afae84)
  - `FALL_THROUGH` [`00afae78`](#insn-00afae78) → [`00afae7c`](#insn-00afae7c)
- ブロック [`00afae7c`](#insn-00afae7c) 範囲 `[['00afae7c', '00afae83']]`
  - `UNCONDITIONAL_JUMP` [`00afae80`](#insn-00afae80) → [`00afaeb0`](#insn-00afaeb0)
- ブロック [`00afae84`](#insn-00afae84) 範囲 `[['00afae84', '00afaeaf']]`
  - `FALL_THROUGH` [`00afaeac`](#insn-00afaeac) → [`00afaeb0`](#insn-00afaeb0)
- ブロック [`00afaeb0`](#insn-00afaeb0) 範囲 `[['00afaeb0', '00afaeb3']]`
  - `FALL_THROUGH` [`00afaeb0`](#insn-00afaeb0) → [`00afaeb4`](#insn-00afaeb4)
- ブロック [`00afaeb4`](#insn-00afaeb4) 範囲 `[['00afaeb4', '00afaeb7']]`
  - `FALL_THROUGH` [`00afaeb4`](#insn-00afaeb4) → [`00afaeb8`](#insn-00afaeb8)
- ブロック [`00afaeb8`](#insn-00afaeb8) 範囲 `[['00afaeb8', '00afaebb']]`

## 命令位置別の参照

- [`00afae4c`](#insn-00afae4c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae50`](#insn-00afae50) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae60`](#insn-00afae60) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afae74`](#insn-00afae74) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afae78`](#insn-00afae78) → [`00afae84`](#insn-00afae84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae80`](#insn-00afae80) → [`00afaeb0`](#insn-00afaeb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae88`](#insn-00afae88) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaeb0`](#insn-00afaeb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaeb4`](#insn-00afaeb4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afae4c`](#insn-00afae4c)

~~~json
{
  "source": "00afae4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae50`](#insn-00afae50)

~~~json
{
  "source": "00afae50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae60`](#insn-00afae60)

~~~json
{
  "source": "00afae60",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae74`](#insn-00afae74)

~~~json
{
  "source": "00afae74",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae78`](#insn-00afae78)

~~~json
{
  "source": "00afae78",
  "target": "00afae84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae80`](#insn-00afae80)

~~~json
{
  "source": "00afae80",
  "target": "00afaeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae88`](#insn-00afae88)

~~~json
{
  "source": "00afae88",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaeb0`](#insn-00afaeb0)

~~~json
{
  "source": "00afaeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaeb4`](#insn-00afaeb4)

~~~json
{
  "source": "00afaeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
