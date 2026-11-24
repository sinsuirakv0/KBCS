# 00a9aacc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9aa88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9aa88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0005.md#compare-83ab0a0ee2d3751c17410e03fce5c227)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0086.md#review-d21391e11d5010a8d0dd143313a854ae)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9aacc",
  "name": "FUN_00a9aacc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9bbc5859b4cf90e9269b4ba266e9ffb7f241356779706355b4be6637d3f16702",
  "source_text_sha256": "9bbc5859b4cf90e9269b4ba266e9ffb7f241356779706355b4be6637d3f16702",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9aacc",
        "00a9ab3b"
      ]
    ],
    "bytes_sha256": "7f1756aa0d0b6947e328a41c7240318106a5b1b5012bd8d1cdc914fbf227c521",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006e4aec](../006e4/006e4aec.md)
- [006e79bc](../006e7/006e79bc.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00a9aacc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x843bc) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9aacc"></a> `00a9aacc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a9aad0"></a> `00a9aad0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9aad4"></a> `00a9aad4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9aad8"></a> `00a9aad8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00a9aadc"></a> `00a9aadc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9aae0"></a> `00a9aae0` | `a8 12 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9aae4"></a> `00a9aae4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00a9aae8"></a> `00a9aae8` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00a9aaec"></a> `00a9aaec` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9aaf0"></a> `00a9aaf0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00a9aaf4"></a> `00a9aaf4` | `07 9f ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9aaf8"></a> `00a9aaf8` | `60 00 00 37` | tbnz w0,#0x0,0x00a9ab04 | `CONDITIONAL_JUMP`
<a id="insn-00a9aafc"></a> `00a9aafc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9ab00"></a> `00a9ab00` | `0c 00 00 14` | b 0x00a9ab30 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ab04"></a> `00a9ab04` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00a9ab08"></a> `00a9ab08` | `9e 12 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ab0c"></a> `00a9ab0c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9ab10"></a> `00a9ab10` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9ab14"></a> `00a9ab14` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9ab18"></a> `00a9ab18` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9ab1c"></a> `00a9ab1c` | `89 77 88 52` | mov w9,#0x43bc | `FALL_THROUGH`
<a id="insn-00a9ab20"></a> `00a9ab20` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ab24"></a> `00a9ab24` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ab28"></a> `00a9ab28` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00a9ab2c"></a> `00a9ab2c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00a9ab30"></a> `00a9ab30` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ab34"></a> `00a9ab34` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a9ab38"></a> `00a9ab38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9aacc`](#insn-00a9aacc) 範囲 `[['00a9aacc', '00a9aafb']]`
  - `CONDITIONAL_JUMP` [`00a9aaf8`](#insn-00a9aaf8) → [`00a9ab04`](#insn-00a9ab04)
  - `FALL_THROUGH` [`00a9aaf8`](#insn-00a9aaf8) → [`00a9aafc`](#insn-00a9aafc)
- ブロック [`00a9aafc`](#insn-00a9aafc) 範囲 `[['00a9aafc', '00a9ab03']]`
  - `UNCONDITIONAL_JUMP` [`00a9ab00`](#insn-00a9ab00) → [`00a9ab30`](#insn-00a9ab30)
- ブロック [`00a9ab04`](#insn-00a9ab04) 範囲 `[['00a9ab04', '00a9ab2f']]`
  - `FALL_THROUGH` [`00a9ab2c`](#insn-00a9ab2c) → [`00a9ab30`](#insn-00a9ab30)
- ブロック [`00a9ab30`](#insn-00a9ab30) 範囲 `[['00a9ab30', '00a9ab3b']]`

## 命令位置別の参照

- [`00a9aacc`](#insn-00a9aacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9aad0`](#insn-00a9aad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9aae0`](#insn-00a9aae0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9aaf4`](#insn-00a9aaf4) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9aaf8`](#insn-00a9aaf8) → [`00a9ab04`](#insn-00a9ab04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ab00`](#insn-00a9ab00) → [`00a9ab30`](#insn-00a9ab30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ab08`](#insn-00a9ab08) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ab30`](#insn-00a9ab30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ab34`](#insn-00a9ab34) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9aacc`](#insn-00a9aacc)

~~~json
{
  "source": "00a9aacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9aad0`](#insn-00a9aad0)

~~~json
{
  "source": "00a9aad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9aae0`](#insn-00a9aae0)

~~~json
{
  "source": "00a9aae0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9aaf4`](#insn-00a9aaf4)

~~~json
{
  "source": "00a9aaf4",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9aaf8`](#insn-00a9aaf8)

~~~json
{
  "source": "00a9aaf8",
  "target": "00a9ab04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ab00`](#insn-00a9ab00)

~~~json
{
  "source": "00a9ab00",
  "target": "00a9ab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ab08`](#insn-00a9ab08)

~~~json
{
  "source": "00a9ab08",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ab30`](#insn-00a9ab30)

~~~json
{
  "source": "00a9ab30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ab34`](#insn-00a9ab34)

~~~json
{
  "source": "00a9ab34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
