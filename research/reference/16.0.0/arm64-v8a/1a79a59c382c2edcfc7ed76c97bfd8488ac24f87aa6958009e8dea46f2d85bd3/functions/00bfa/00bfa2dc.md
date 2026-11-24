# 00bfa2dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7d894`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-f2923b6e759a170f904614132c9b12a3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa704`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-d4653a9ed23ee2516ba3ef92dc556d83)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa2dc",
  "name": "_ZNSt6__ndk16thread4joinEv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487",
  "source_text_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa2dc",
        "00bfa327"
      ]
    ],
    "bytes_sha256": "d3594d4057f08b88296b65d9d1ed4ef655e18ad39d183f38b09c2e9f6312ec9b",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57d70](../00c57/00c57d70.md)

## 呼び出し先

- [00c57d20](../00c57/00c57d20.md)
- [00c5d240](../00c5d/00c5d240.md)

## 関連文字列（未確認候補）

~~~text
"thread::join failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 378 bytes

~~~c

void _ZNSt6__ndk16thread4joinEv(pthread_t *param_1)

{
  int iVar1;
  
  if (*param_1 == 0) {
    iVar1 = 0x16;
  }
  else {
    iVar1 = pthread_join(*param_1,(void **)0x0);
    if (iVar1 == 0) {
      *param_1 = 0;
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"thread::join failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa2dc"></a> `00bfa2dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa2e0"></a> `00bfa2e0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfa2e4"></a> `00bfa2e4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa2e8"></a> `00bfa2e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa2ec"></a> `00bfa2ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa2f0"></a> `00bfa2f0` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bfa2f4"></a> `00bfa2f4` | `20 01 00 b4` | cbz x0,0x00bfa318 | `CONDITIONAL_JUMP`
<a id="insn-00bfa2f8"></a> `00bfa2f8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bfa2fc"></a> `00bfa2fc` | `d1 8b 01 94` | bl 0x00c5d240 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa300"></a> `00bfa300` | `e0 00 00 35` | cbnz w0,0x00bfa31c | `CONDITIONAL_JUMP`
<a id="insn-00bfa304"></a> `00bfa304` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bfa308"></a> `00bfa308` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa30c"></a> `00bfa30c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa310"></a> `00bfa310` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa314"></a> `00bfa314` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfa318"></a> `00bfa318` | `c0 02 80 52` | mov w0,#0x16 | `FALL_THROUGH`
<a id="insn-00bfa31c"></a> `00bfa31c` | `61 b5 ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bfa320"></a> `00bfa320` | `21 2c 08 91` | add x1,x1,#0x20b | `FALL_THROUGH`
<a id="insn-00bfa324"></a> `00bfa324` | `7f 76 01 94` | bl 0x00c57d20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa2dc`](#insn-00bfa2dc) 範囲 `[['00bfa2dc', '00bfa2f7']]`
  - `CONDITIONAL_JUMP` [`00bfa2f4`](#insn-00bfa2f4) → [`00bfa318`](#insn-00bfa318)
  - `FALL_THROUGH` [`00bfa2f4`](#insn-00bfa2f4) → [`00bfa2f8`](#insn-00bfa2f8)
- ブロック [`00bfa2f8`](#insn-00bfa2f8) 範囲 `[['00bfa2f8', '00bfa303']]`
  - `CONDITIONAL_JUMP` [`00bfa300`](#insn-00bfa300) → [`00bfa31c`](#insn-00bfa31c)
  - `FALL_THROUGH` [`00bfa300`](#insn-00bfa300) → [`00bfa304`](#insn-00bfa304)
- ブロック [`00bfa304`](#insn-00bfa304) 範囲 `[['00bfa304', '00bfa317']]`
- ブロック [`00bfa318`](#insn-00bfa318) 範囲 `[['00bfa318', '00bfa31b']]`
  - `FALL_THROUGH` [`00bfa318`](#insn-00bfa318) → [`00bfa31c`](#insn-00bfa31c)
- ブロック [`00bfa31c`](#insn-00bfa31c) 範囲 `[['00bfa31c', '00bfa327']]`

## 命令位置別の参照

- [`00bfa2e0`](#insn-00bfa2e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa2e4`](#insn-00bfa2e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa2f4`](#insn-00bfa2f4) → [`00bfa318`](#insn-00bfa318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa2fc`](#insn-00bfa2fc) → [`00c5d240`](../00c5d/00c5d240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d240` · 推定シンボル `None` · 推定型 `None`
- [`00bfa300`](#insn-00bfa300) → [`00bfa31c`](#insn-00bfa31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa308`](#insn-00bfa308) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa30c`](#insn-00bfa30c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa320`](#insn-00bfa320) → `002a620b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfa324`](#insn-00bfa324) → [`00c57d20`](../00c57/00c57d20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57d20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa2e0`](#insn-00bfa2e0)

~~~json
{
  "source": "00bfa2e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa2e4`](#insn-00bfa2e4)

~~~json
{
  "source": "00bfa2e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa2f4`](#insn-00bfa2f4)

~~~json
{
  "source": "00bfa2f4",
  "target": "00bfa318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa2fc`](#insn-00bfa2fc)

~~~json
{
  "source": "00bfa2fc",
  "target": "00c5d240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa300`](#insn-00bfa300)

~~~json
{
  "source": "00bfa300",
  "target": "00bfa31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa308`](#insn-00bfa308)

~~~json
{
  "source": "00bfa308",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa30c`](#insn-00bfa30c)

~~~json
{
  "source": "00bfa30c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa320`](#insn-00bfa320)

~~~json
{
  "source": "00bfa320",
  "target": "002a620b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a620b",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "7468726561643a3a6a6f696e206661696c656400",
  "capture_start": "002a620b",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfa324`](#insn-00bfa324)

~~~json
{
  "source": "00bfa324",
  "target": "00c57d20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
