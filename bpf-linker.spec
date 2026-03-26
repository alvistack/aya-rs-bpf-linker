# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: bpf-linker
Epoch: 100
Version: 0.10.1
Release: 1%{?dist}
Summary: Simple BPF static linker
License: Apache-2.0
URL: https://github.com/aya-rs/bpf-linker/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: rust

%description
bpf-linker aims to simplify building modern BPF programs while still
supporting older, more restrictive kernels.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
RUSTC_BOOTSTRAP=1 \
cargo build --locked --offline --release --no-default-features --features llvm-21

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -t %{buildroot}%{_bindir} target/release/bpf-linker

%files
%license LICENSE-APACHE
%{_bindir}/bpf-linker

%changelog
