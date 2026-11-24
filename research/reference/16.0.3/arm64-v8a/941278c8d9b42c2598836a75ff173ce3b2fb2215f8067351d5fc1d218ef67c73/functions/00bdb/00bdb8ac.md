# 00bdb8ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bda8b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-e0f89d23ed5fe0c32edd074a7a1c416d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdb8ac",
  "name": "_ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba18306884232b3b50d7c26c635b9c9edd3b0c5597c57b4ed90e9242e5c79ba1",
  "source_text_sha256": "ba18306884232b3b50d7c26c635b9c9edd3b0c5597c57b4ed90e9242e5c79ba1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdb8ac",
        "00bdb917"
      ]
    ],
    "bytes_sha256": "607b8023c48200139f311435842b906837f1534a104d3582877ae61f2e4edd3b",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 486 bytes

~~~c

bool _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_
               (undefined8 *param_1,undefined8 *param_2)

{
  char cVar1;
  long lVar2;
  long *plVar3;
  
  lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar2 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
  cVar1 = (**(code **)(*plVar3 + 0xc0))(plVar3,*(undefined8 *)*param_1,*(undefined8 *)*param_2);
  return cVar1 != '\0';
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdb8ac"></a> `00bdb8ac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdb8b0"></a> `00bdb8b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdb8b4"></a> `00bdb8b4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdb8b8"></a> `00bdb8b8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdb8bc"></a> `00bdb8bc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bdb8c0"></a> `00bdb8c0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdb8c4"></a> `00bdb8c4` | `8f 02 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb8c8"></a> `00bdb8c8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdb8cc"></a> `00bdb8cc` | `80 00 00 b5` | cbnz x0,0x00bdb8dc | `CONDITIONAL_JUMP`
<a id="insn-00bdb8d0"></a> `00bdb8d0` | `a0 b6 ff f0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdb8d4"></a> `00bdb8d4` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdb8d8"></a> `00bdb8d8` | `f2 01 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb8dc"></a> `00bdb8dc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdb8e0"></a> `00bdb8e0` | `10 02 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb8e4"></a> `00bdb8e4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdb8e8"></a> `00bdb8e8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bdb8ec"></a> `00bdb8ec` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bdb8f0"></a> `00bdb8f0` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bdb8f4"></a> `00bdb8f4` | `22 01 40 f9` | ldr x2,[x9] | `FALL_THROUGH`
<a id="insn-00bdb8f8"></a> `00bdb8f8` | `48 61 40 f9` | ldr x8,[x10, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdb8fc"></a> `00bdb8fc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb900"></a> `00bdb900` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdb904"></a> `00bdb904` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdb908"></a> `00bdb908` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdb90c"></a> `00bdb90c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bdb910"></a> `00bdb910` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdb914"></a> `00bdb914` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdb8ac`](#insn-00bdb8ac) 範囲 `[['00bdb8ac', '00bdb8cf']]`
  - `CONDITIONAL_JUMP` [`00bdb8cc`](#insn-00bdb8cc) → [`00bdb8dc`](#insn-00bdb8dc)
  - `FALL_THROUGH` [`00bdb8cc`](#insn-00bdb8cc) → [`00bdb8d0`](#insn-00bdb8d0)
- ブロック [`00bdb8d0`](#insn-00bdb8d0) 範囲 `[['00bdb8d0', '00bdb8db']]`
  - `FALL_THROUGH` [`00bdb8d8`](#insn-00bdb8d8) → [`00bdb8dc`](#insn-00bdb8dc)
- ブロック [`00bdb8dc`](#insn-00bdb8dc) 範囲 `[['00bdb8dc', '00bdb917']]`

## 命令位置別の参照

- [`00bdb8ac`](#insn-00bdb8ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8b0`](#insn-00bdb8b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8b4`](#insn-00bdb8b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8c4`](#insn-00bdb8c4) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8cc`](#insn-00bdb8cc) → [`00bdb8dc`](#insn-00bdb8dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8d4`](#insn-00bdb8d4) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdb8d8`](#insn-00bdb8d8) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdb8e0`](#insn-00bdb8e0) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdb900`](#insn-00bdb900) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb904`](#insn-00bdb904) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdb8ac`](#insn-00bdb8ac)

~~~json
{
  "source": "00bdb8ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb8b0`](#insn-00bdb8b0)

~~~json
{
  "source": "00bdb8b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb8b4`](#insn-00bdb8b4)

~~~json
{
  "source": "00bdb8b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb8c4`](#insn-00bdb8c4)

~~~json
{
  "source": "00bdb8c4",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb8cc`](#insn-00bdb8cc)

~~~json
{
  "source": "00bdb8cc",
  "target": "00bdb8dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb8d4`](#insn-00bdb8d4)

~~~json
{
  "source": "00bdb8d4",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdb8d8`](#insn-00bdb8d8)

~~~json
{
  "source": "00bdb8d8",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb8e0`](#insn-00bdb8e0)

~~~json
{
  "source": "00bdb8e0",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb900`](#insn-00bdb900)

~~~json
{
  "source": "00bdb900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb904`](#insn-00bdb904)

~~~json
{
  "source": "00bdb904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
