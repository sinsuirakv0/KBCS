# 00aa4aec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa4aa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4aa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-62155d75019471efb775cdca7f2a4533)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0089.md#review-2cde4c8624ac0b6a0bef50127ad2fb46)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa4aec",
  "name": "FUN_00aa4aec",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0649215b830093f9f5ea50c77ec6617883d0c56393cbfb98a60f161fd58e860",
  "source_text_sha256": "f0649215b830093f9f5ea50c77ec6617883d0c56393cbfb98a60f161fd58e860",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa4aec",
        "00aa4b4f"
      ]
    ],
    "bytes_sha256": "1ef5fad308a4d632b6036361f58bab7114b638bd8705dfcf7994d83fd7896b88",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0069ef54](../0069e/0069ef54.md)
- [009f1ea8](../009f1/009f1ea8.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 467 bytes

~~~c

bool FUN_00aa4aec(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa4af4 to 00ba4b4f has its CatchHandler @ 00aa59b4 */
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(&uleb128_0023a2c4 + lVar2 + (long)param_2 * 0x1c4) != 0;
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
<a id="insn-00aa4aec"></a> `00aa4aec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aa4af0"></a> `00aa4af0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa4af4"></a> `00aa4af4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa4af8"></a> `00aa4af8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aa4afc"></a> `00aa4afc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa4b00"></a> `00aa4b00` | `a0 ea f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa4b04"></a> `00aa4b04` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa4b08"></a> `00aa4b08` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa4b0c"></a> `00aa4b0c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa4b10"></a> `00aa4b10` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa4b14"></a> `00aa4b14` | `ff 76 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa4b18"></a> `00aa4b18` | `40 01 00 37` | tbnz w0,#0x0,0x00aa4b40 | `CONDITIONAL_JUMP`
<a id="insn-00aa4b1c"></a> `00aa4b1c` | `99 ea f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa4b20"></a> `00aa4b20` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa4b24"></a> `00aa4b24` | `89 58 94 52` | mov w9,#0xa2c4 | `FALL_THROUGH`
<a id="insn-00aa4b28"></a> `00aa4b28` | `68 02 28 9b` | smaddl x8,w19,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa4b2c"></a> `00aa4b2c` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa4b30"></a> `00aa4b30` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa4b34"></a> `00aa4b34` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aa4b38"></a> `00aa4b38` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00aa4b3c"></a> `00aa4b3c` | `02 00 00 14` | b 0x00aa4b44 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa4b40"></a> `00aa4b40` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa4b44"></a> `00aa4b44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa4b48"></a> `00aa4b48` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aa4b4c"></a> `00aa4b4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa4aec`](#insn-00aa4aec) 範囲 `[['00aa4aec', '00aa4af3']]`
  - `FALL_THROUGH` [`00aa4af0`](#insn-00aa4af0) → [`00aa4af4`](#insn-00aa4af4)
- ブロック [`00aa4af4`](#insn-00aa4af4) 範囲 `[['00aa4af4', '00aa4b1b']]`
  - `CONDITIONAL_JUMP` [`00aa4b18`](#insn-00aa4b18) → [`00aa4b40`](#insn-00aa4b40)
  - `FALL_THROUGH` [`00aa4b18`](#insn-00aa4b18) → [`00aa4b1c`](#insn-00aa4b1c)
- ブロック [`00aa4b1c`](#insn-00aa4b1c) 範囲 `[['00aa4b1c', '00aa4b3f']]`
  - `UNCONDITIONAL_JUMP` [`00aa4b3c`](#insn-00aa4b3c) → [`00aa4b44`](#insn-00aa4b44)
- ブロック [`00aa4b40`](#insn-00aa4b40) 範囲 `[['00aa4b40', '00aa4b43']]`
  - `FALL_THROUGH` [`00aa4b40`](#insn-00aa4b40) → [`00aa4b44`](#insn-00aa4b44)
- ブロック [`00aa4b44`](#insn-00aa4b44) 範囲 `[['00aa4b44', '00aa4b4f']]`

## 命令位置別の参照

- [`00aa4aec`](#insn-00aa4aec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa4af0`](#insn-00aa4af0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b00`](#insn-00aa4b00) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b14`](#insn-00aa4b14) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b18`](#insn-00aa4b18) → [`00aa4b40`](#insn-00aa4b40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b1c`](#insn-00aa4b1c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b30`](#insn-00aa4b30) → `0023a2c4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00aa4b3c`](#insn-00aa4b3c) → [`00aa4b44`](#insn-00aa4b44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b44`](#insn-00aa4b44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa4b48`](#insn-00aa4b48) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa4aec`](#insn-00aa4aec)

~~~json
{
  "source": "00aa4aec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa4af0`](#insn-00aa4af0)

~~~json
{
  "source": "00aa4af0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa4b00`](#insn-00aa4b00)

~~~json
{
  "source": "00aa4b00",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa4b14`](#insn-00aa4b14)

~~~json
{
  "source": "00aa4b14",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa4b18`](#insn-00aa4b18)

~~~json
{
  "source": "00aa4b18",
  "target": "00aa4b40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa4b1c`](#insn-00aa4b1c)

~~~json
{
  "source": "00aa4b1c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa4b30`](#insn-00aa4b30)

~~~json
{
  "source": "00aa4b30",
  "target": "0023a2c4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023a2c4",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0023a2c4",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa4b3c`](#insn-00aa4b3c)

~~~json
{
  "source": "00aa4b3c",
  "target": "00aa4b44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa4b44`](#insn-00aa4b44)

~~~json
{
  "source": "00aa4b44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa4b48`](#insn-00aa4b48)

~~~json
{
  "source": "00aa4b48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
