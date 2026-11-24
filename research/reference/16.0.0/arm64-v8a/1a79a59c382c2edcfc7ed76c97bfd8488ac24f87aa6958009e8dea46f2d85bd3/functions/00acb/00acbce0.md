# 00acbce0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6dd4c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd4c.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/no_difference_in_scope-0008.md#compare-1f60d97f06a3ec9fbee891a3b3f9e4ca)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbedc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbedc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0005.md#compare-48b9bfc1a80400bebd8ff0a9d7c46994)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbce0",
  "name": "FUN_00acbce0",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f160912622d3e3e7f1931a0add23f0f25332bb32a6753c41fce813db89c126b3",
  "source_text_sha256": "f160912622d3e3e7f1931a0add23f0f25332bb32a6753c41fce813db89c126b3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbce0",
        "00acbd1b"
      ]
    ],
    "bytes_sha256": "7e7e1cda346a3bbb3103eba76ed8c923a01ef901c1edd08adfe9a5a12457a4fb",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00731fec](../00731/00731fec.md)
- [00935974](../00935/00935974.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 458 bytes

~~~c

int FUN_00acbce0(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 0xc) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 0xc) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbce0"></a> `00acbce0` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbce4"></a> `00acbce4` | `49 01 00 b4` | cbz x9,0x00acbd0c | `CONDITIONAL_JUMP`
<a id="insn-00acbce8"></a> `00acbce8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbcec"></a> `00acbcec` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbcf0"></a> `00acbcf0` | `4a 0d 40 b9` | ldr w10,[x10, #0xc] | `FALL_THROUGH`
<a id="insn-00acbcf4"></a> `00acbcf4` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00acbcf8"></a> `00acbcf8` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00acbcfc"></a> `00acbcfc` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acbd00"></a> `00acbd00` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbd04"></a> `00acbd04` | `69 ff ff b5` | cbnz x9,0x00acbcf0 | `CONDITIONAL_JUMP`
<a id="insn-00acbd08"></a> `00acbd08` | `02 00 00 14` | b 0x00acbd10 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd0c"></a> `00acbd0c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbd10"></a> `00acbd10` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acbd14"></a> `00acbd14` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00acbd18"></a> `00acbd18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbce0`](#insn-00acbce0) 範囲 `[['00acbce0', '00acbce7']]`
  - `CONDITIONAL_JUMP` [`00acbce4`](#insn-00acbce4) → [`00acbd0c`](#insn-00acbd0c)
  - `FALL_THROUGH` [`00acbce4`](#insn-00acbce4) → [`00acbce8`](#insn-00acbce8)
- ブロック [`00acbce8`](#insn-00acbce8) 範囲 `[['00acbce8', '00acbcef']]`
  - `FALL_THROUGH` [`00acbcec`](#insn-00acbcec) → [`00acbcf0`](#insn-00acbcf0)
- ブロック [`00acbcf0`](#insn-00acbcf0) 範囲 `[['00acbcf0', '00acbd07']]`
  - `CONDITIONAL_JUMP` [`00acbd04`](#insn-00acbd04) → [`00acbcf0`](#insn-00acbcf0)
  - `FALL_THROUGH` [`00acbd04`](#insn-00acbd04) → [`00acbd08`](#insn-00acbd08)
- ブロック [`00acbd08`](#insn-00acbd08) 範囲 `[['00acbd08', '00acbd0b']]`
  - `UNCONDITIONAL_JUMP` [`00acbd08`](#insn-00acbd08) → [`00acbd10`](#insn-00acbd10)
- ブロック [`00acbd0c`](#insn-00acbd0c) 範囲 `[['00acbd0c', '00acbd0f']]`
  - `FALL_THROUGH` [`00acbd0c`](#insn-00acbd0c) → [`00acbd10`](#insn-00acbd10)
- ブロック [`00acbd10`](#insn-00acbd10) 範囲 `[['00acbd10', '00acbd1b']]`

## 命令位置別の参照

- [`00acbce4`](#insn-00acbce4) → [`00acbd0c`](#insn-00acbd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd04`](#insn-00acbd04) → [`00acbcf0`](#insn-00acbcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd08`](#insn-00acbd08) → [`00acbd10`](#insn-00acbd10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbce4`](#insn-00acbce4)

~~~json
{
  "source": "00acbce4",
  "target": "00acbd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd04`](#insn-00acbd04)

~~~json
{
  "source": "00acbd04",
  "target": "00acbcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd08`](#insn-00acbd08)

~~~json
{
  "source": "00acbd08",
  "target": "00acbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
