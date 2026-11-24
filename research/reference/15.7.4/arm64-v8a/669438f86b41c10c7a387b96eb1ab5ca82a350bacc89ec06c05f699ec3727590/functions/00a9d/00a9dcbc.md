# 00a9dcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9dc78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9dc78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-b3741f7379d4c57adf3968cf468b1ac8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0087.md#review-51d6c749c2c182788cea42a75ed4ccc8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9dcbc",
  "name": "FUN_00a9dcbc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d67f69fd8b550b395c44cf12ce6b2cce8564298f8ce7f33383dc517cad175541",
  "source_text_sha256": "d67f69fd8b550b395c44cf12ce6b2cce8564298f8ce7f33383dc517cad175541",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9dcbc",
        "00a9dd2b"
      ]
    ],
    "bytes_sha256": "a08e4d98571e99c907215a38f1a1937293738cb92e43ba0dd293178dda6e2664",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00a9dcbc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8422c) != 0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9dcbc"></a> `00a9dcbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a9dcc0"></a> `00a9dcc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9dcc4"></a> `00a9dcc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9dcc8"></a> `00a9dcc8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00a9dccc"></a> `00a9dccc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9dcd0"></a> `00a9dcd0` | `2c 06 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9dcd4"></a> `00a9dcd4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00a9dcd8"></a> `00a9dcd8` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00a9dcdc"></a> `00a9dcdc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9dce0"></a> `00a9dce0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00a9dce4"></a> `00a9dce4` | `8b 92 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9dce8"></a> `00a9dce8` | `a0 01 00 37` | tbnz w0,#0x0,0x00a9dd1c | `CONDITIONAL_JUMP`
<a id="insn-00a9dcec"></a> `00a9dcec` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00a9dcf0"></a> `00a9dcf0` | `24 06 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9dcf4"></a> `00a9dcf4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9dcf8"></a> `00a9dcf8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9dcfc"></a> `00a9dcfc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9dd00"></a> `00a9dd00` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9dd04"></a> `00a9dd04` | `89 45 88 52` | mov w9,#0x422c | `FALL_THROUGH`
<a id="insn-00a9dd08"></a> `00a9dd08` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9dd0c"></a> `00a9dd0c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9dd10"></a> `00a9dd10` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00a9dd14"></a> `00a9dd14` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00a9dd18"></a> `00a9dd18` | `02 00 00 14` | b 0x00a9dd20 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9dd1c"></a> `00a9dd1c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9dd20"></a> `00a9dd20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9dd24"></a> `00a9dd24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a9dd28"></a> `00a9dd28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9dcbc`](#insn-00a9dcbc) 範囲 `[['00a9dcbc', '00a9dceb']]`
  - `CONDITIONAL_JUMP` [`00a9dce8`](#insn-00a9dce8) → [`00a9dd1c`](#insn-00a9dd1c)
  - `FALL_THROUGH` [`00a9dce8`](#insn-00a9dce8) → [`00a9dcec`](#insn-00a9dcec)
- ブロック [`00a9dcec`](#insn-00a9dcec) 範囲 `[['00a9dcec', '00a9dd1b']]`
  - `UNCONDITIONAL_JUMP` [`00a9dd18`](#insn-00a9dd18) → [`00a9dd20`](#insn-00a9dd20)
- ブロック [`00a9dd1c`](#insn-00a9dd1c) 範囲 `[['00a9dd1c', '00a9dd1f']]`
  - `FALL_THROUGH` [`00a9dd1c`](#insn-00a9dd1c) → [`00a9dd20`](#insn-00a9dd20)
- ブロック [`00a9dd20`](#insn-00a9dd20) 範囲 `[['00a9dd20', '00a9dd2b']]`

## 命令位置別の参照

- [`00a9dcbc`](#insn-00a9dcbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9dcc0`](#insn-00a9dcc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9dcd0`](#insn-00a9dcd0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9dce4`](#insn-00a9dce4) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9dce8`](#insn-00a9dce8) → [`00a9dd1c`](#insn-00a9dd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9dcf0`](#insn-00a9dcf0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9dd18`](#insn-00a9dd18) → [`00a9dd20`](#insn-00a9dd20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9dd20`](#insn-00a9dd20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9dd24`](#insn-00a9dd24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9dcbc`](#insn-00a9dcbc)

~~~json
{
  "source": "00a9dcbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9dcc0`](#insn-00a9dcc0)

~~~json
{
  "source": "00a9dcc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9dcd0`](#insn-00a9dcd0)

~~~json
{
  "source": "00a9dcd0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9dce4`](#insn-00a9dce4)

~~~json
{
  "source": "00a9dce4",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9dce8`](#insn-00a9dce8)

~~~json
{
  "source": "00a9dce8",
  "target": "00a9dd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9dcf0`](#insn-00a9dcf0)

~~~json
{
  "source": "00a9dcf0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9dd18`](#insn-00a9dd18)

~~~json
{
  "source": "00a9dd18",
  "target": "00a9dd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9dd20`](#insn-00a9dd20)

~~~json
{
  "source": "00a9dd20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9dd24`](#insn-00a9dd24)

~~~json
{
  "source": "00a9dd24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
