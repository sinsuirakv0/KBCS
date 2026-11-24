# 009dfdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009dfc10`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009dfc10.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0032.md#compare-3321426f6d042b3ef56d9f1c1dd4d2bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009dfe00`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe00.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0031.md#compare-dc0354fa57f5f0d7e798dfade3f1e7bf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dfdac",
  "name": "FUN_009dfdac",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8",
  "source_text_sha256": "df6dc82b76bdef2cca79aa2572a4787c1d0144aae74bfc68abba5809326f2fc8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dfdac",
        "009dfe0b"
      ]
    ],
    "bytes_sha256": "3b6316be63ba81f9b4807545408da5b64c1ca4a5f89cfbe44b02bbeeddd0f22f",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad0958](../00ad0/00ad0958.md)

## 呼び出し先

- [005c179c](../005c1/005c179c.md)
- [009dfb18](../009df/009dfb18.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 419 bytes

~~~c

bool FUN_009dfdac(void)

{
  long lVar1;
  undefined1 auStack_40 [8];
  undefined8 local_38;
  ulong uStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_009dfb18(auStack_40);
  FUN_005c179c(auStack_40,local_38);
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return 1 < uStack_30;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dfdac"></a> `009dfdac` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-009dfdb0"></a> `009dfdb0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dfdb4"></a> `009dfdb4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dfdb8"></a> `009dfdb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009dfdbc"></a> `009dfdbc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009dfdc0"></a> `009dfdc0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009dfdc4"></a> `009dfdc4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009dfdc8"></a> `009dfdc8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-009dfdcc"></a> `009dfdcc` | `53 ff ff 97` | bl 0x009dfb18 | `UNCONDITIONAL_CALL`
<a id="insn-009dfdd0"></a> `009dfdd0` | `e1 a3 40 a9` | ldp x1,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009dfdd4"></a> `009dfdd4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-009dfdd8"></a> `009dfdd8` | `1f 05 00 f1` | cmp x8,#0x1 | `FALL_THROUGH`
<a id="insn-009dfddc"></a> `009dfddc` | `f3 97 9f 1a` | cset w19,hi | `FALL_THROUGH`
<a id="insn-009dfde0"></a> `009dfde0` | `6f 86 ef 97` | bl 0x005c179c | `UNCONDITIONAL_CALL`
<a id="insn-009dfde4"></a> `009dfde4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009dfde8"></a> `009dfde8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009dfdec"></a> `009dfdec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009dfdf0"></a> `009dfdf0` | `c1 00 00 54` | b.ne 0x009dfe08 | `CONDITIONAL_JUMP`
<a id="insn-009dfdf4"></a> `009dfdf4` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-009dfdf8"></a> `009dfdf8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dfdfc"></a> `009dfdfc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dfe00"></a> `009dfe00` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-009dfe04"></a> `009dfe04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009dfe08"></a> `009dfe08` | `36 e0 09 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009dfdac`](#insn-009dfdac) 範囲 `[['009dfdac', '009dfdf3']]`
  - `CONDITIONAL_JUMP` [`009dfdf0`](#insn-009dfdf0) → [`009dfe08`](#insn-009dfe08)
  - `FALL_THROUGH` [`009dfdf0`](#insn-009dfdf0) → [`009dfdf4`](#insn-009dfdf4)
- ブロック [`009dfdf4`](#insn-009dfdf4) 範囲 `[['009dfdf4', '009dfe07']]`
- ブロック [`009dfe08`](#insn-009dfe08) 範囲 `[['009dfe08', '009dfe0b']]`

## 命令位置別の参照

- [`009dfdb0`](#insn-009dfdb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdb4`](#insn-009dfdb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdc4`](#insn-009dfdc4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdcc`](#insn-009dfdcc) → [`009dfb18`](009dfb18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009dfb18` · 推定シンボル `None` · 推定型 `None`
- [`009dfdd0`](#insn-009dfdd0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfde0`](#insn-009dfde0) → [`005c179c`](../005c1/005c179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c179c` · 推定シンボル `None` · 推定型 `None`
- [`009dfde8`](#insn-009dfde8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdf0`](#insn-009dfdf0) → [`009dfe08`](#insn-009dfe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdf8`](#insn-009dfdf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfdfc`](#insn-009dfdfc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dfe08`](#insn-009dfe08) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dfdb0`](#insn-009dfdb0)

~~~json
{
  "source": "009dfdb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdb4`](#insn-009dfdb4)

~~~json
{
  "source": "009dfdb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdc4`](#insn-009dfdc4)

~~~json
{
  "source": "009dfdc4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdcc`](#insn-009dfdcc)

~~~json
{
  "source": "009dfdcc",
  "target": "009dfb18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dfdd0`](#insn-009dfdd0)

~~~json
{
  "source": "009dfdd0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfde0`](#insn-009dfde0)

~~~json
{
  "source": "009dfde0",
  "target": "005c179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dfde8`](#insn-009dfde8)

~~~json
{
  "source": "009dfde8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdf0`](#insn-009dfdf0)

~~~json
{
  "source": "009dfdf0",
  "target": "009dfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdf8`](#insn-009dfdf8)

~~~json
{
  "source": "009dfdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfdfc`](#insn-009dfdfc)

~~~json
{
  "source": "009dfdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dfe08`](#insn-009dfe08)

~~~json
{
  "source": "009dfe08",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
