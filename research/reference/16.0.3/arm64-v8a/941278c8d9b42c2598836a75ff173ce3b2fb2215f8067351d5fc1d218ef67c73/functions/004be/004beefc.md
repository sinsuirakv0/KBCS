# 004beefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bebdc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-d10cd7ea5fc7abd7e69e94166e3246d4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004beefc",
  "name": "_ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e834c2464785b3f6cde02248ec5948b035ccd4f6f5b05d7ff91cc279f2f4e65",
  "source_text_sha256": "8e834c2464785b3f6cde02248ec5948b035ccd4f6f5b05d7ff91cc279f2f4e65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004beefc",
        "004bef9f"
      ],
      [
        "004befcc",
        "004befcf"
      ]
    ],
    "bytes_sha256": "d6e6f93179b39fb9886355a355528294c69e78340c3c99eef393828300f36ee6",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459830](../00459/00459830.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59e40](../00c59/00c59e40.md)

## 関連文字列（未確認候補）

~~~text
"CPUID flags: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 828 bytes

~~~c

void _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE(undefined8 param_1)

{
  long lVar1;
  undefined1 *puVar2;
  undefined8 uVar3;
  byte local_50;
  undefined1 auStack_4f [7];
  ulong local_48;
  undefined1 *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar3 = FUN_00459830(param_1,"CPUID flags: ",0xd);
  _ZN5Botan5CPUID9to_stringEv(&local_50);
  puVar2 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar2 = auStack_4f;
  }
  uVar3 = FUN_00459830(uVar3,puVar2,local_48);
  FUN_00459830(uVar3,&DAT_002b4cef,1);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004beefc"></a> `004beefc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004bef00"></a> `004bef00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bef04"></a> `004bef04` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bef08"></a> `004bef08` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bef0c"></a> `004bef0c` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004bef10"></a> `004bef10` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bef14"></a> `004bef14` | `41 ef ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-004bef18"></a> `004bef18` | `21 10 1b 91` | add x1,x1,#0x6c4 | `FALL_THROUGH`
<a id="insn-004bef1c"></a> `004bef1c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004bef20"></a> `004bef20` | `a2 01 80 52` | mov w2,#0xd | `FALL_THROUGH`
<a id="insn-004bef24"></a> `004bef24` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bef28"></a> `004bef28` | `42 6a fe 97` | bl 0x00459830 | `UNCONDITIONAL_CALL`
<a id="insn-004bef2c"></a> `004bef2c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004bef30"></a> `004bef30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bef34"></a> `004bef34` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-004bef38"></a> `004bef38` | `c2 6b 1e 94` | bl 0x00c59e40 | `UNCONDITIONAL_CALL`
<a id="insn-004bef3c"></a> `004bef3c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004bef40"></a> `004bef40` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bef44"></a> `004bef44` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004bef48"></a> `004bef48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004bef4c"></a> `004bef4c` | `21 15 95 9a` | csinc x1,x9,x21,ne | `FALL_THROUGH`
<a id="insn-004bef50"></a> `004bef50` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-004bef54"></a> `004bef54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bef58"></a> `004bef58` | `36 6a fe 97` | bl 0x00459830 | `UNCONDITIONAL_CALL`
<a id="insn-004bef5c"></a> `004bef5c` | `a1 ef ff d0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-004bef60"></a> `004bef60` | `21 bc 33 91` | add x1,x1,#0xcef | `FALL_THROUGH`
<a id="insn-004bef64"></a> `004bef64` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004bef68"></a> `004bef68` | `32 6a fe 97` | bl 0x00459830 | `UNCONDITIONAL_CALL`
<a id="insn-004bef6c"></a> `004bef6c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004bef70"></a> `004bef70` | `68 00 00 36` | tbz w8,#0x0,0x004bef7c | `CONDITIONAL_JUMP`
<a id="insn-004bef74"></a> `004bef74` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bef78"></a> `004bef78` | `f6 67 1e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004bef7c"></a> `004bef7c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004bef80"></a> `004bef80` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bef84"></a> `004bef84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bef88"></a> `004bef88` | `21 02 00 54` | b.ne 0x004befcc | `CONDITIONAL_JUMP`
<a id="insn-004bef8c"></a> `004bef8c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bef90"></a> `004bef90` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bef94"></a> `004bef94` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bef98"></a> `004bef98` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004bef9c"></a> `004bef9c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004befcc"></a> `004befcc` | `ed 67 1e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004beefc`](#insn-004beefc) 範囲 `[['004beefc', '004bef73']]`
  - `CONDITIONAL_JUMP` [`004bef70`](#insn-004bef70) → [`004bef7c`](#insn-004bef7c)
  - `FALL_THROUGH` [`004bef70`](#insn-004bef70) → [`004bef74`](#insn-004bef74)
- ブロック [`004bef74`](#insn-004bef74) 範囲 `[['004bef74', '004bef7b']]`
  - `FALL_THROUGH` [`004bef78`](#insn-004bef78) → [`004bef7c`](#insn-004bef7c)
- ブロック [`004bef7c`](#insn-004bef7c) 範囲 `[['004bef7c', '004bef8b']]`
  - `CONDITIONAL_JUMP` [`004bef88`](#insn-004bef88) → [`004befcc`](#insn-004befcc)
  - `FALL_THROUGH` [`004bef88`](#insn-004bef88) → [`004bef8c`](#insn-004bef8c)
- ブロック [`004bef8c`](#insn-004bef8c) 範囲 `[['004bef8c', '004bef9f']]`
- ブロック [`004befcc`](#insn-004befcc) 範囲 `[['004befcc', '004befcf']]`

## 命令位置別の参照

- [`004bef00`](#insn-004bef00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef04`](#insn-004bef04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef08`](#insn-004bef08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef18`](#insn-004bef18) → `002a66c4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bef24`](#insn-004bef24) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef28`](#insn-004bef28) → [`00459830`](../00459/00459830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459830` · 推定シンボル `None` · 推定型 `None`
- [`004bef38`](#insn-004bef38) → [`00c59e40`](../00c59/00c59e40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59e40` · 推定シンボル `None` · 推定型 `None`
- [`004bef3c`](#insn-004bef3c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef40`](#insn-004bef40) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef58`](#insn-004bef58) → [`00459830`](../00459/00459830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459830` · 推定シンボル `None` · 推定型 `None`
- [`004bef60`](#insn-004bef60) → `002b4cef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef68`](#insn-004bef68) → [`00459830`](../00459/00459830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459830` · 推定シンボル `None` · 推定型 `None`
- [`004bef6c`](#insn-004bef6c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef70`](#insn-004bef70) → [`004bef7c`](#insn-004bef7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef74`](#insn-004bef74) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef78`](#insn-004bef78) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004bef80`](#insn-004bef80) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef88`](#insn-004bef88) → [`004befcc`](#insn-004befcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef8c`](#insn-004bef8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef90`](#insn-004bef90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef94`](#insn-004bef94) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004befcc`](#insn-004befcc) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bef00`](#insn-004bef00)

~~~json
{
  "source": "004bef00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef04`](#insn-004bef04)

~~~json
{
  "source": "004bef04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef08`](#insn-004bef08)

~~~json
{
  "source": "004bef08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef18`](#insn-004bef18)

~~~json
{
  "source": "004bef18",
  "target": "002a66c4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a66c4",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "435055494420666c6167733a2000",
  "capture_start": "002a66c4",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bef24`](#insn-004bef24)

~~~json
{
  "source": "004bef24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef28`](#insn-004bef28)

~~~json
{
  "source": "004bef28",
  "target": "00459830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bef38`](#insn-004bef38)

~~~json
{
  "source": "004bef38",
  "target": "00c59e40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bef3c`](#insn-004bef3c)

~~~json
{
  "source": "004bef3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef40`](#insn-004bef40)

~~~json
{
  "source": "004bef40",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef58`](#insn-004bef58)

~~~json
{
  "source": "004bef58",
  "target": "00459830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bef60`](#insn-004bef60)

~~~json
{
  "source": "004bef60",
  "target": "002b4cef",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef68`](#insn-004bef68)

~~~json
{
  "source": "004bef68",
  "target": "00459830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bef6c`](#insn-004bef6c)

~~~json
{
  "source": "004bef6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef70`](#insn-004bef70)

~~~json
{
  "source": "004bef70",
  "target": "004bef7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef74`](#insn-004bef74)

~~~json
{
  "source": "004bef74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef78`](#insn-004bef78)

~~~json
{
  "source": "004bef78",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bef80`](#insn-004bef80)

~~~json
{
  "source": "004bef80",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef88`](#insn-004bef88)

~~~json
{
  "source": "004bef88",
  "target": "004befcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef8c`](#insn-004bef8c)

~~~json
{
  "source": "004bef8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef90`](#insn-004bef90)

~~~json
{
  "source": "004bef90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef94`](#insn-004bef94)

~~~json
{
  "source": "004bef94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004befcc`](#insn-004befcc)

~~~json
{
  "source": "004befcc",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
