# 00b7cbdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7cca4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0003.md#compare-ed15b6283ada351f3f19be1423b55667)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7cbdc",
  "name": "_ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6da5b9de47dcf212eb21c17e9a43563b83c4f90e38e2d1ce7addb9c34dcb0fcd",
  "source_text_sha256": "6da5b9de47dcf212eb21c17e9a43563b83c4f90e38e2d1ce7addb9c34dcb0fcd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7cbdc",
        "00b7cc33"
      ]
    ],
    "bytes_sha256": "1f92f4fbf8d1adc1e76a1a1b4b63893b0b442c1cc63eb9f0634b30c902e32139",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb5d0](../00bdb/00bdb5d0.md)

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1a0](../00bdb/00bdb1a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 464 bytes

~~~c

void _ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE(long *param_1,long param_2)

{
  uint uVar1;
  
  *param_1 = param_2;
  _ZNSt6__ndk15mutex4lockEv(param_2 + 0x18);
  uVar1 = *(uint *)(param_2 + 0x70);
  if ((uVar1 >> 1 & 1) == 0) {
    FUN_00bd6d60(1,param_2 + 8);
    *(uint *)(param_2 + 0x70) = uVar1 | 2;
    _ZNSt6__ndk15mutex6unlockEv(param_2 + 0x18);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7cbdc"></a> `00b7cbdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7cbe0"></a> `00b7cbe0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b7cbe4"></a> `00b7cbe4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cbe8"></a> `00b7cbe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7cbec"></a> `00b7cbec` | `01 00 00 f9` | str x1,[x0] | `FALL_THROUGH`
<a id="insn-00b7cbf0"></a> `00b7cbf0` | `20 60 00 91` | add x0,x1,#0x18 | `FALL_THROUGH`
<a id="insn-00b7cbf4"></a> `00b7cbf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b7cbf8"></a> `00b7cbf8` | `66 79 01 94` | bl 0x00bdb190 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cbfc"></a> `00b7cbfc` | `74 72 40 b9` | ldr w20,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00b7cc00"></a> `00b7cc00` | `74 01 08 37` | tbnz w20,#0x1,0x00b7cc2c | `CONDITIONAL_JUMP`
<a id="insn-00b7cc04"></a> `00b7cc04` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b7cc08"></a> `00b7cc08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cc0c"></a> `00b7cc0c` | `55 68 01 94` | bl 0x00bd6d60 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cc10"></a> `00b7cc10` | `88 02 1f 32` | orr w8,w20,#0x2 | `FALL_THROUGH`
<a id="insn-00b7cc14"></a> `00b7cc14` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00b7cc18"></a> `00b7cc18` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00b7cc1c"></a> `00b7cc1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cc20"></a> `00b7cc20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b7cc24"></a> `00b7cc24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7cc28"></a> `00b7cc28` | `5e 79 01 14` | b 0x00bdb1a0 | `CALL_TERMINATOR`
<a id="insn-00b7cc2c"></a> `00b7cc2c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cc30"></a> `00b7cc30` | `f3 ea e2 97` | bl 0x004377fc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7cbdc`](#insn-00b7cbdc) 範囲 `[['00b7cbdc', '00b7cc03']]`
  - `CONDITIONAL_JUMP` [`00b7cc00`](#insn-00b7cc00) → [`00b7cc2c`](#insn-00b7cc2c)
  - `FALL_THROUGH` [`00b7cc00`](#insn-00b7cc00) → [`00b7cc04`](#insn-00b7cc04)
- ブロック [`00b7cc04`](#insn-00b7cc04) 範囲 `[['00b7cc04', '00b7cc2b']]`
- ブロック [`00b7cc2c`](#insn-00b7cc2c) 範囲 `[['00b7cc2c', '00b7cc33']]`

## 命令位置別の参照

- [`00b7cbe0`](#insn-00b7cbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbe4`](#insn-00b7cbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbf8`](#insn-00b7cbf8) → [`00bdb190`](../00bdb/00bdb190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb190` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc00`](#insn-00b7cc00) → [`00b7cc2c`](#insn-00b7cc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc0c`](#insn-00b7cc0c) → [`00bd6d60`](../00bd6/00bd6d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d60` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc1c`](#insn-00b7cc1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc20`](#insn-00b7cc20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc28`](#insn-00b7cc28) → [`00bdb1a0`](../00bdb/00bdb1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc30`](#insn-00b7cc30) → [`004377fc`](../00437/004377fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004377fc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7cbe0`](#insn-00b7cbe0)

~~~json
{
  "source": "00b7cbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cbe4`](#insn-00b7cbe4)

~~~json
{
  "source": "00b7cbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cbf8`](#insn-00b7cbf8)

~~~json
{
  "source": "00b7cbf8",
  "target": "00bdb190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc00`](#insn-00b7cc00)

~~~json
{
  "source": "00b7cc00",
  "target": "00b7cc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc0c`](#insn-00b7cc0c)

~~~json
{
  "source": "00b7cc0c",
  "target": "00bd6d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc1c`](#insn-00b7cc1c)

~~~json
{
  "source": "00b7cc1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc20`](#insn-00b7cc20)

~~~json
{
  "source": "00b7cc20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc28`](#insn-00b7cc28)

~~~json
{
  "source": "00b7cc28",
  "target": "00bdb1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc30`](#insn-00b7cc30)

~~~json
{
  "source": "00b7cc30",
  "target": "004377fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
