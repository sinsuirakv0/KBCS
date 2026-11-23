# 00b0edbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0ee84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ee84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0002.md#compare-4448a6eb0f8898531230cb1953b0277a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0edbc",
  "name": "_ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "526837294ef7c76c6897889cfd7d09d9b4fe24c3135eea067c8f684130c2aa8c",
  "source_text_sha256": "526837294ef7c76c6897889cfd7d09d9b4fe24c3135eea067c8f684130c2aa8c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0edbc",
        "00b0ee2b"
      ]
    ],
    "bytes_sha256": "f9cde46a4f2534e4afc4a60c0d78255cca9a2dc989dc44c52aea48b97be594cb",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdf8d0](../00bdf/00bdf8d0.md)

## 関連文字列（未確認候補）

~~~text
"warning: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1607 bytes

~~~c

void _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (undefined8 param_1)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_40,"warning: ");
  _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0ee28 to 00c0eef7 has its CatchHandler @ 00b0ee28
                       catch() { ... } // from try @ 00b0ee28 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0ef18 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f028 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f0a8 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f17c with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f2b0 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f4b4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f5d4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f744 with catch @ 00b0ee28 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0edbc"></a> `00b0edbc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b0edc0"></a> `00b0edc0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0edc4"></a> `00b0edc4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0edc8"></a> `00b0edc8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b0edcc"></a> `00b0edcc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b0edd0"></a> `00b0edd0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b0edd4"></a> `00b0edd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0edd8"></a> `00b0edd8` | `00 bc ff f0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b0eddc"></a> `00b0eddc` | `00 ec 14 91` | add x0,x0,#0x53b | `FALL_THROUGH`
<a id="insn-00b0ede0"></a> `00b0ede0` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b0ede4"></a> `00b0ede4` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b0ede8"></a> `00b0ede8` | `de 30 03 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00b0edec"></a> `00b0edec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b0edf0"></a> `00b0edf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0edf4"></a> `00b0edf4` | `b7 42 03 94` | bl 0x00bdf8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0edf8"></a> `00b0edf8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b0edfc"></a> `00b0edfc` | `68 00 00 36` | tbz w8,#0x0,0x00b0ee08 | `CONDITIONAL_JUMP`
<a id="insn-00b0ee00"></a> `00b0ee00` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ee04"></a> `00b0ee04` | `57 30 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ee08"></a> `00b0ee08` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b0ee0c"></a> `00b0ee0c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b0ee10"></a> `00b0ee10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b0ee14"></a> `00b0ee14` | `a1 00 00 54` | b.ne 0x00b0ee28 | `CONDITIONAL_JUMP`
<a id="insn-00b0ee18"></a> `00b0ee18` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0ee1c"></a> `00b0ee1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ee20"></a> `00b0ee20` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b0ee24"></a> `00b0ee24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0ee28"></a> `00b0ee28` | `5a 30 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0edbc`](#insn-00b0edbc) 範囲 `[['00b0edbc', '00b0edff']]`
  - `CONDITIONAL_JUMP` [`00b0edfc`](#insn-00b0edfc) → [`00b0ee08`](#insn-00b0ee08)
  - `FALL_THROUGH` [`00b0edfc`](#insn-00b0edfc) → [`00b0ee00`](#insn-00b0ee00)
- ブロック [`00b0ee00`](#insn-00b0ee00) 範囲 `[['00b0ee00', '00b0ee07']]`
  - `FALL_THROUGH` [`00b0ee04`](#insn-00b0ee04) → [`00b0ee08`](#insn-00b0ee08)
- ブロック [`00b0ee08`](#insn-00b0ee08) 範囲 `[['00b0ee08', '00b0ee17']]`
  - `CONDITIONAL_JUMP` [`00b0ee14`](#insn-00b0ee14) → [`00b0ee28`](#insn-00b0ee28)
  - `FALL_THROUGH` [`00b0ee14`](#insn-00b0ee14) → [`00b0ee18`](#insn-00b0ee18)
- ブロック [`00b0ee18`](#insn-00b0ee18) 範囲 `[['00b0ee18', '00b0ee27']]`
- ブロック [`00b0ee28`](#insn-00b0ee28) 範囲 `[['00b0ee28', '00b0ee2b']]`

## 命令位置別の参照

- [`00b0edc0`](#insn-00b0edc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edc4`](#insn-00b0edc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eddc`](#insn-00b0eddc) → `0029153b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ede0`](#insn-00b0ede0) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ede8`](#insn-00b0ede8) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00b0edf4`](#insn-00b0edf4) → [`00bdf8d0`](../00bdf/00bdf8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf8d0` · 推定シンボル `None` · 推定型 `None`
- [`00b0edf8`](#insn-00b0edf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edfc`](#insn-00b0edfc) → [`00b0ee08`](#insn-00b0ee08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee00`](#insn-00b0ee00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee04`](#insn-00b0ee04) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee0c`](#insn-00b0ee0c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee14`](#insn-00b0ee14) → [`00b0ee28`](#insn-00b0ee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee18`](#insn-00b0ee18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee1c`](#insn-00b0ee1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ee28`](#insn-00b0ee28) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0edc0`](#insn-00b0edc0)

~~~json
{
  "source": "00b0edc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edc4`](#insn-00b0edc4)

~~~json
{
  "source": "00b0edc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eddc`](#insn-00b0eddc)

~~~json
{
  "source": "00b0eddc",
  "target": "0029153b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029153b",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "7761726e696e673a2000",
  "capture_start": "0029153b",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0ede0`](#insn-00b0ede0)

~~~json
{
  "source": "00b0ede0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ede8`](#insn-00b0ede8)

~~~json
{
  "source": "00b0ede8",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0edf4`](#insn-00b0edf4)

~~~json
{
  "source": "00b0edf4",
  "target": "00bdf8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0edf8`](#insn-00b0edf8)

~~~json
{
  "source": "00b0edf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edfc`](#insn-00b0edfc)

~~~json
{
  "source": "00b0edfc",
  "target": "00b0ee08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee00`](#insn-00b0ee00)

~~~json
{
  "source": "00b0ee00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee04`](#insn-00b0ee04)

~~~json
{
  "source": "00b0ee04",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ee0c`](#insn-00b0ee0c)

~~~json
{
  "source": "00b0ee0c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee14`](#insn-00b0ee14)

~~~json
{
  "source": "00b0ee14",
  "target": "00b0ee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee18`](#insn-00b0ee18)

~~~json
{
  "source": "00b0ee18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee1c`](#insn-00b0ee1c)

~~~json
{
  "source": "00b0ee1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ee28`](#insn-00b0ee28)

~~~json
{
  "source": "00b0ee28",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
