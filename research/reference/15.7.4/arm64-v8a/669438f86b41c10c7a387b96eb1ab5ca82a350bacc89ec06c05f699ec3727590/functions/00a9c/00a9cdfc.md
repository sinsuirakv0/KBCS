# 00a9cdfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9cdb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cdb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0005.md#compare-f34d71b6e30d5adb0fc7ef3e8a3a5784)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0087.md#review-5188cc3eef9b6212ac274b69cffed38e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9cdfc",
  "name": "FUN_00a9cdfc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fd4fafc93ea5c76fa068c0c047d814f9efe7cc9e611448c56918f1de443d7d2",
  "source_text_sha256": "1fd4fafc93ea5c76fa068c0c047d814f9efe7cc9e611448c56918f1de443d7d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9cdfc",
        "00a9ce4f"
      ]
    ],
    "bytes_sha256": "87b3b337003fa480bea5a41982bde61fa3cb502898d1b4a3da91dd9f5b7239b6",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ce03c](../005ce/005ce03c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00a9cdfc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84324) = *(int *)(lVar1 + 0x84324) + param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9cdfc"></a> `00a9cdfc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a9ce00"></a> `00a9ce00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ce04"></a> `00a9ce04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ce08"></a> `00a9ce08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9ce0c"></a> `00a9ce0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00a9ce10"></a> `00a9ce10` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00a9ce14"></a> `00a9ce14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00a9ce18"></a> `00a9ce18` | `da 09 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ce1c"></a> `00a9ce1c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9ce20"></a> `00a9ce20` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9ce24"></a> `00a9ce24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9ce28"></a> `00a9ce28` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9ce2c"></a> `00a9ce2c` | `89 64 88 52` | mov w9,#0x4324 | `FALL_THROUGH`
<a id="insn-00a9ce30"></a> `00a9ce30` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ce34"></a> `00a9ce34` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ce38"></a> `00a9ce38` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00a9ce3c"></a> `00a9ce3c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ce40"></a> `00a9ce40` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ce44"></a> `00a9ce44` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ce48"></a> `00a9ce48` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a9ce4c"></a> `00a9ce4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9cdfc`](#insn-00a9cdfc) 範囲 `[['00a9cdfc', '00a9ce4f']]`

## 命令位置別の参照

- [`00a9cdfc`](#insn-00a9cdfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce00`](#insn-00a9ce00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce04`](#insn-00a9ce04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce18`](#insn-00a9ce18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce40`](#insn-00a9ce40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce44`](#insn-00a9ce44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ce48`](#insn-00a9ce48) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9cdfc`](#insn-00a9cdfc)

~~~json
{
  "source": "00a9cdfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ce00`](#insn-00a9ce00)

~~~json
{
  "source": "00a9ce00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ce04`](#insn-00a9ce04)

~~~json
{
  "source": "00a9ce04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ce18`](#insn-00a9ce18)

~~~json
{
  "source": "00a9ce18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ce40`](#insn-00a9ce40)

~~~json
{
  "source": "00a9ce40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ce44`](#insn-00a9ce44)

~~~json
{
  "source": "00a9ce44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ce48`](#insn-00a9ce48)

~~~json
{
  "source": "00a9ce48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
