# 00bfa7ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa750`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-f84d7a1b98e5580447e10ce1f3cc744d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfb7e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb7e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-c1d6a1f9e4e37083ffb856431a10e0aa)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa7ec",
  "name": "_ZNSt6__ndk16thread6detachEv",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8e133cc68e739b2283608f947ad481d46ceb7d2aadcb7c968af47c10216e317",
  "source_text_sha256": "e8e133cc68e739b2283608f947ad481d46ceb7d2aadcb7c968af47c10216e317",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa7ec",
        "00bfa833"
      ]
    ],
    "bytes_sha256": "e66d719e175a46bc33336055b710f4072a07ce3cbb19bdbadb05fcdc13830190",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c585e0](../00c58/00c585e0.md)

## 呼び出し先

- [00c581f0](../00c58/00c581f0.md)
- [00c5e350](../00c5e/00c5e350.md)

## 関連文字列（未確認候補）

~~~text
"thread::detach failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 371 bytes

~~~c

void _ZNSt6__ndk16thread6detachEv(pthread_t *param_1)

{
  int iVar1;
  
  if (*param_1 == 0) {
    iVar1 = 0x16;
  }
  else {
    iVar1 = pthread_detach(*param_1);
    if (iVar1 == 0) {
      *param_1 = 0;
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"thread::detach failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa7ec"></a> `00bfa7ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa7f0"></a> `00bfa7f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfa7f4"></a> `00bfa7f4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa7f8"></a> `00bfa7f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa7fc"></a> `00bfa7fc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfa800"></a> `00bfa800` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bfa804"></a> `00bfa804` | `00 01 00 b4` | cbz x0,0x00bfa824 | `CONDITIONAL_JUMP`
<a id="insn-00bfa808"></a> `00bfa808` | `d2 8e 01 94` | bl 0x00c5e350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa80c"></a> `00bfa80c` | `e0 00 00 35` | cbnz w0,0x00bfa828 | `CONDITIONAL_JUMP`
<a id="insn-00bfa810"></a> `00bfa810` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bfa814"></a> `00bfa814` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfa818"></a> `00bfa818` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfa81c"></a> `00bfa81c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa820"></a> `00bfa820` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfa824"></a> `00bfa824` | `c0 02 80 52` | mov w0,#0x16 | `FALL_THROUGH`
<a id="insn-00bfa828"></a> `00bfa828` | `a1 b5 ff 90` | adrp x1,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bfa82c"></a> `00bfa82c` | `21 bc 13 91` | add x1,x1,#0x4ef | `FALL_THROUGH`
<a id="insn-00bfa830"></a> `00bfa830` | `70 76 01 94` | bl 0x00c581f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa7ec`](#insn-00bfa7ec) 範囲 `[['00bfa7ec', '00bfa807']]`
  - `CONDITIONAL_JUMP` [`00bfa804`](#insn-00bfa804) → [`00bfa824`](#insn-00bfa824)
  - `FALL_THROUGH` [`00bfa804`](#insn-00bfa804) → [`00bfa808`](#insn-00bfa808)
- ブロック [`00bfa808`](#insn-00bfa808) 範囲 `[['00bfa808', '00bfa80f']]`
  - `CONDITIONAL_JUMP` [`00bfa80c`](#insn-00bfa80c) → [`00bfa828`](#insn-00bfa828)
  - `FALL_THROUGH` [`00bfa80c`](#insn-00bfa80c) → [`00bfa810`](#insn-00bfa810)
- ブロック [`00bfa810`](#insn-00bfa810) 範囲 `[['00bfa810', '00bfa823']]`
- ブロック [`00bfa824`](#insn-00bfa824) 範囲 `[['00bfa824', '00bfa827']]`
  - `FALL_THROUGH` [`00bfa824`](#insn-00bfa824) → [`00bfa828`](#insn-00bfa828)
- ブロック [`00bfa828`](#insn-00bfa828) 範囲 `[['00bfa828', '00bfa833']]`

## 命令位置別の参照

- [`00bfa7f0`](#insn-00bfa7f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa7f4`](#insn-00bfa7f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa804`](#insn-00bfa804) → [`00bfa824`](#insn-00bfa824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa808`](#insn-00bfa808) → [`00c5e350`](../00c5e/00c5e350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e350` · 推定シンボル `None` · 推定型 `None`
- [`00bfa80c`](#insn-00bfa80c) → [`00bfa828`](#insn-00bfa828) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa814`](#insn-00bfa814) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa818`](#insn-00bfa818) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa82c`](#insn-00bfa82c) → `002ae4ef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfa830`](#insn-00bfa830) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa7f0`](#insn-00bfa7f0)

~~~json
{
  "source": "00bfa7f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa7f4`](#insn-00bfa7f4)

~~~json
{
  "source": "00bfa7f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa804`](#insn-00bfa804)

~~~json
{
  "source": "00bfa804",
  "target": "00bfa824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa808`](#insn-00bfa808)

~~~json
{
  "source": "00bfa808",
  "target": "00c5e350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa80c`](#insn-00bfa80c)

~~~json
{
  "source": "00bfa80c",
  "target": "00bfa828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa814`](#insn-00bfa814)

~~~json
{
  "source": "00bfa814",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa818`](#insn-00bfa818)

~~~json
{
  "source": "00bfa818",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa82c`](#insn-00bfa82c)

~~~json
{
  "source": "00bfa82c",
  "target": "002ae4ef",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae4ef",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "7468726561643a3a646574616368206661696c656400",
  "capture_start": "002ae4ef",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfa830`](#insn-00bfa830)

~~~json
{
  "source": "00bfa830",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
