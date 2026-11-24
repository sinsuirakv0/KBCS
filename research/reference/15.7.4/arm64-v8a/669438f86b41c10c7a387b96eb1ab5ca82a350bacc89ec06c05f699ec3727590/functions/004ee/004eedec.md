# 004eedec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004eedec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004eedec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0006.md#compare-5d49b0a58848c277a134bcedb22f358e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00511c84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511c84.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0008.md#compare-78e24fb8b5ef3cdd4b4a6e0ac0f5d329)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eedec",
  "name": "_ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbc4a4365a9bde7dda2d1faec967f76dd65484b8010c1d47b7df8dca4152c3a1",
  "source_text_sha256": "cbc4a4365a9bde7dda2d1faec967f76dd65484b8010c1d47b7df8dca4152c3a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004eedec",
        "004eee73"
      ],
      [
        "004eee98",
        "004eee9b"
      ]
    ],
    "bytes_sha256": "f67007cffdc0c5728015f78d7774068870dedc2490f7ed410f991f2aeac2cb37",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)
- [00bdb730](../00bdb/00bdb730.md)
- [00bdcf20](../00bdc/00bdcf20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 885 bytes

~~~c

void _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZNSt6__ndk16chrono12system_clock3nowEv();
  local_60 = 0;
  uStack_58 = 0;
  local_50 = 0;
  _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE
            (param_1,param_2,&local_60,1,param_3,uVar2,param_4);
  if (*(long *)(lVar1 + 0x28) == local_48) {
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
<a id="insn-004eedec"></a> `004eedec` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004eedf0"></a> `004eedf0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004eedf4"></a> `004eedf4` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004eedf8"></a> `004eedf8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004eedfc"></a> `004eedfc` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004eee00"></a> `004eee00` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004eee04"></a> `004eee04` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004eee08"></a> `004eee08` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-004eee0c"></a> `004eee0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-004eee10"></a> `004eee10` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004eee14"></a> `004eee14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004eee18"></a> `004eee18` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004eee1c"></a> `004eee1c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eee20"></a> `004eee20` | `44 b2 1b 94` | bl 0x00bdb730 | `UNCONDITIONAL_CALL`
<a id="insn-004eee24"></a> `004eee24` | `e4 03 00 aa` | mov x4,x0 | `FALL_THROUGH`
<a id="insn-004eee28"></a> `004eee28` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-004eee2c"></a> `004eee2c` | `e5 03 13 2a` | mov w5,w19 | `FALL_THROUGH`
<a id="insn-004eee30"></a> `004eee30` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004eee34"></a> `004eee34` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004eee38"></a> `004eee38` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-004eee3c"></a> `004eee3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004eee40"></a> `004eee40` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004eee44"></a> `004eee44` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-004eee48"></a> `004eee48` | `36 b8 1b 94` | bl 0x00bdcf20 | `UNCONDITIONAL_CALL`
<a id="insn-004eee4c"></a> `004eee4c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004eee50"></a> `004eee50` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eee54"></a> `004eee54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004eee58"></a> `004eee58` | `01 02 00 54` | b.ne 0x004eee98 | `CONDITIONAL_JUMP`
<a id="insn-004eee5c"></a> `004eee5c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004eee60"></a> `004eee60` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004eee64"></a> `004eee64` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004eee68"></a> `004eee68` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004eee6c"></a> `004eee6c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004eee70"></a> `004eee70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004eee98"></a> `004eee98` | `7e b0 1b 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004eedec`](#insn-004eedec) 範囲 `[['004eedec', '004eee5b']]`
  - `CONDITIONAL_JUMP` [`004eee58`](#insn-004eee58) → [`004eee98`](#insn-004eee98)
  - `FALL_THROUGH` [`004eee58`](#insn-004eee58) → [`004eee5c`](#insn-004eee5c)
- ブロック [`004eee5c`](#insn-004eee5c) 範囲 `[['004eee5c', '004eee73']]`
- ブロック [`004eee98`](#insn-004eee98) 範囲 `[['004eee98', '004eee9b']]`

## 命令位置別の参照

- [`004eedf0`](#insn-004eedf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eedf4`](#insn-004eedf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eedf8`](#insn-004eedf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eedfc`](#insn-004eedfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee1c`](#insn-004eee1c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee20`](#insn-004eee20) → [`00bdb730`](../00bdb/00bdb730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb730` · 推定シンボル `None` · 推定型 `None`
- [`004eee28`](#insn-004eee28) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee30`](#insn-004eee30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee48`](#insn-004eee48) → [`00bdcf20`](../00bdc/00bdcf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdcf20` · 推定シンボル `None` · 推定型 `None`
- [`004eee50`](#insn-004eee50) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee58`](#insn-004eee58) → [`004eee98`](#insn-004eee98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee5c`](#insn-004eee5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee60`](#insn-004eee60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee64`](#insn-004eee64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee68`](#insn-004eee68) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eee98`](#insn-004eee98) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004eedf0`](#insn-004eedf0)

~~~json
{
  "source": "004eedf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eedf4`](#insn-004eedf4)

~~~json
{
  "source": "004eedf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eedf8`](#insn-004eedf8)

~~~json
{
  "source": "004eedf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eedfc`](#insn-004eedfc)

~~~json
{
  "source": "004eedfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee1c`](#insn-004eee1c)

~~~json
{
  "source": "004eee1c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee20`](#insn-004eee20)

~~~json
{
  "source": "004eee20",
  "target": "00bdb730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eee28`](#insn-004eee28)

~~~json
{
  "source": "004eee28",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee30`](#insn-004eee30)

~~~json
{
  "source": "004eee30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee48`](#insn-004eee48)

~~~json
{
  "source": "004eee48",
  "target": "00bdcf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eee50`](#insn-004eee50)

~~~json
{
  "source": "004eee50",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee58`](#insn-004eee58)

~~~json
{
  "source": "004eee58",
  "target": "004eee98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee5c`](#insn-004eee5c)

~~~json
{
  "source": "004eee5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee60`](#insn-004eee60)

~~~json
{
  "source": "004eee60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee64`](#insn-004eee64)

~~~json
{
  "source": "004eee64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee68`](#insn-004eee68)

~~~json
{
  "source": "004eee68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eee98`](#insn-004eee98)

~~~json
{
  "source": "004eee98",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
