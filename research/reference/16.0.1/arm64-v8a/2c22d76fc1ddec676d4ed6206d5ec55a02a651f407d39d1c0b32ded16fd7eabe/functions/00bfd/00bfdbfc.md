# 00bfdbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfd7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-82819b04d7b72f42f48a524212f61790)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdc98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-95c990e922c8b87a0911922bd8648247)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdbfc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f57dc6c5697719541ae289046a2e30ef9ef39c4647f81513be31e499328c20d",
  "source_text_sha256": "3f57dc6c5697719541ae289046a2e30ef9ef39c4647f81513be31e499328c20d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdbfc",
        "00bfdc8b"
      ]
    ],
    "bytes_sha256": "a4e2dd530c13f083a4b551e6a1d79b12f11eee1ef3a38997379c824799c7deba",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c5e390](../00c5e/00c5e390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 644 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  undefined4 uVar1;
  long *plVar2;
  undefined1 auStack_38 [8];
  
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
  uVar1 = (**(code **)(*plVar2 + 0x38))(plVar2,10);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc(param_1,param_2,param_3,uVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfdbfc"></a> `00bfdbfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdc00"></a> `00bfdc00` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfdc04"></a> `00bfdc04` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdc08"></a> `00bfdc08` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdc0c"></a> `00bfdc0c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdc10"></a> `00bfdc10` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfdc14"></a> `00bfdc14` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdc18"></a> `00bfdc18` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfdc1c"></a> `00bfdc1c` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bfdc20"></a> `00bfdc20` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfdc24"></a> `00bfdc24` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdc28"></a> `00bfdc28` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfdc2c"></a> `00bfdc2c` | `00 00 09 8b` | add x0,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfdc30"></a> `00bfdc30` | `90 69 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdc34"></a> `00bfdc34` | `e1 04 00 b0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfdc38"></a> `00bfdc38` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfdc3c"></a> `00bfdc3c` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00bfdc40"></a> `00bfdc40` | `90 69 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdc44"></a> `00bfdc44` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdc48"></a> `00bfdc48` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfdc4c"></a> `00bfdc4c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00bfdc50"></a> `00bfdc50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdc54"></a> `00bfdc54` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bfdc58"></a> `00bfdc58` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfdc5c"></a> `00bfdc5c` | `8d 69 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdc60"></a> `00bfdc60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfdc64"></a> `00bfdc64` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bfdc68"></a> `00bfdc68` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bfdc6c"></a> `00bfdc6c` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00bfdc70"></a> `00bfdc70` | `c8 81 01 94` | bl 0x00c5e390 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdc74"></a> `00bfdc74` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdc78"></a> `00bfdc78` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdc7c"></a> `00bfdc7c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdc80"></a> `00bfdc80` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfdc84"></a> `00bfdc84` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfdc88"></a> `00bfdc88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdbfc`](#insn-00bfdbfc) 範囲 `[['00bfdbfc', '00bfdc8b']]`

## 命令位置別の参照

- [`00bfdc04`](#insn-00bfdc04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc08`](#insn-00bfdc08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc0c`](#insn-00bfdc0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc30`](#insn-00bfdc30) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc3c`](#insn-00bfdc3c) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfdc3c`](#insn-00bfdc3c) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfdc40`](#insn-00bfdc40) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc5c`](#insn-00bfdc5c) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc70`](#insn-00bfdc70) → [`00c5e390`](../00c5e/00c5e390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e390` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc74`](#insn-00bfdc74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc78`](#insn-00bfdc78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc7c`](#insn-00bfdc7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdc04`](#insn-00bfdc04)

~~~json
{
  "source": "00bfdc04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc08`](#insn-00bfdc08)

~~~json
{
  "source": "00bfdc08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc0c`](#insn-00bfdc0c)

~~~json
{
  "source": "00bfdc0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc30`](#insn-00bfdc30)

~~~json
{
  "source": "00bfdc30",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdc3c`](#insn-00bfdc3c)

~~~json
{
  "source": "00bfdc3c",
  "target": "00c9ac30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfdc3c`](#insn-00bfdc3c)

~~~json
{
  "source": "00bfdc3c",
  "target": "01127e18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfdc40`](#insn-00bfdc40)

~~~json
{
  "source": "00bfdc40",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdc5c`](#insn-00bfdc5c)

~~~json
{
  "source": "00bfdc5c",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdc70`](#insn-00bfdc70)

~~~json
{
  "source": "00bfdc70",
  "target": "00c5e390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdc74`](#insn-00bfdc74)

~~~json
{
  "source": "00bfdc74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc78`](#insn-00bfdc78)

~~~json
{
  "source": "00bfdc78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc7c`](#insn-00bfdc7c)

~~~json
{
  "source": "00bfdc7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
